from urllib.parse import urlencode
from urllib.request import Request, urlopen
from datetime import datetime
import json
import inspect
from models import stocks, indices

from config import FT_API_KEY, GUARDIAN_API_KEY


def orderArticles(articles, search_term_queried):
    # if the SUBTITLE contains the first keyword then 
    for article in articles:
        if  search_term_queried in article['subtitle']:
            articles.insert(0, articles.pop(articles.index(article)))
        
    # if the TITLE contains the first keyword then 
    for article in articles:
        if search_term_queried in article['title']:
            articles.insert(0, articles.pop(articles.index(article)))
    return articles

def requestFromFT(start_date, end_date, search_term):
    url = 'https://api.ft.com/content/search/v1?'
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': FT_API_KEY,
    }

    query_string = (
        search_term + ' AND '
        + 'lastPublishDateTime:>' 
        + start_date.strftime('%Y-%m-%dT00:00:00Z') + ' AND '
        + 'lastPublishDateTime:<' 
        + end_date.strftime('%Y-%m-%dT00:00:00Z')
    )
    body = {
        'queryString': query_string,
        'resultContext': {
            'aspects': [
                'title', 
                'lifecycle', 
                'editorial'
            ]
        }
    }
    print('request:  ' + str(body))
    encoded_body = json.dumps(body).encode('utf-8')

    ft_request = Request(url, encoded_body, headers)
    with urlopen(ft_request) as f:
        ft_result = f.read()
    return json.loads(ft_result.decode())

def requestFromGuardian(start_date, end_date, search):
    url = 'https://content.guardianapis.com/search?'
    query_string = (
        'q=' + search
        + '&format=json'
        + '&from-date=' + datetime.strftime(start_date, '%Y-%m-%d')
        + '&to-date=' + datetime.strftime(end_date, '%Y-%m-%d')
        + '&show-fields=headline,trailText'
        + '&order-by=relevance'
        + '&api-key=' + GUARDIAN_API_KEY
    )
    print(url + query_string)
    guardian_request = Request(url + query_string)
    with urlopen(guardian_request) as g:
        guardian_result = g.read()
    guardian_result = json.loads(guardian_result.decode())
    if guardian_result['response']['total'] == 0:
        return None
    articles_in_response = False
    for guardian_article in guardian_result['response']['results']:
        if guardian_article['type'] == 'article':
            articles_in_response = True
    if not articles_in_response:
        return None
    return guardian_result

    

def articleRequestWrapper(request):
    request_json = request.get_json(force=True)
    print('request json from FE: ' + str(request_json))

    instrument = request_json['instrument']
    commodity_name = request_json['name']
    start_date = datetime.strptime(request_json['start'], '%d-%m-%Y')
    end_date = datetime.strptime(request_json['end'], '%d-%m-%Y')
    search_term = request_json['tag']

    # instrument switch
    specific_search = ''
    if(instrument == 's'):
        stock = stocks.query.filter_by(url_name= commodity_name).first()
        initial_search = stock.display_name
        specific_search = stock.specific_tag
        broad_search = stock.broad_tag
    elif(instrument == 'i'):
        index = indices.query.filter_by(symbol= commodity_name).first()
        initial_search = index.search_tag
        broad_search = index.country
    #elif(instrument == 'f'):
        
    
    # make sure that most specific search is done
    if(broad_search != '' and specific_search == ''):
        specific_search = broad_search
        broad_search = 'asdfasdfasdf'
    if(specific_search != '' and initial_search == ''):
        initial_search = specific_search
        specific_search = 'asdfasdfasdf'

    ft_articles = []
    try:
        if(search_term != ''):
            # search term enterd by user, only search for this
            ft_result = requestFromFT(start_date, end_date, search_term)
            search_term_queried = search_term
            if not ft_result['results'][0]['indexCount'] > 0:
                ft_articles = 'no results'
        else:
            # run through the search terms
            ft_result = requestFromFT(start_date, end_date, initial_search)
            search_term_queried = initial_search
            if ft_result['results'][0]['indexCount'] == 0:
                search_term_queried = specific_search
                ft_result = requestFromFT(start_date, end_date, specific_search)
                if ft_result['results'][0]['indexCount'] == 0:
                    search_term_queried = broad_search
                    ft_result = requestFromFT(start_date, end_date, broad_search)
                    if ft_result['results'][0]['indexCount'] == 0:
                        ft_articles = 'no results'

        # Enter into dictionary for response
        if not ft_articles == 'no results':
            for result in ft_result['results'][0]['results']:
                if(result['aspectSet'] == 'article'):
                    ft_articles.append({
                        'title': result['title']['title'],
                        'subtitle': result['editorial']['subheading'],
                        'url_id': result['id'],
                        'publish_date': result['lifecycle']['lastPublishDateTime'] 
                    })
            ft_articles = orderArticles(ft_articles, search_term_queried)
    except Exception as e:
        print(str(e))
        return str(e)


    # Guardian
    guardian_articles = []
    initial_search = '"' + initial_search.replace(' ', '%20') + '"'  
    specific_search = '"' + specific_search.replace(' ', '%20') + '"'
    broad_search = '"' + broad_search.replace(' ', '%20') + '"'
    try:
        if(search_term != ''):
            # search term enterd by user, only search for this
            guardian_result = requestFromGuardian(start_date, end_date, search_term)
            search_term_queried = search_term
            if not ft_result['results'][0]['indexCount'] > 0:
                guardian_articles = 'no results'
        else:
            # run through the search terms
            guardian_result = requestFromGuardian(start_date, end_date, initial_search)
            search_term_queried = initial_search
            if not guardian_result:
                search_term_queried = specific_search
                guardian_result = requestFromGuardian(start_date, end_date, specific_search)
                if not guardian_result:
                    search_term_queried = broad_search
                    guardian_result = requestFromGuardian(start_date, end_date, broad_search)
                    if not guardian_result:
                        guardian_articles = 'no results'
                    
        # Enter into dictionary for response
        if not guardian_articles == 'no results':
            for g_article in guardian_result['response']['results']:
                guardian_articles.append({
                    'title': g_article['fields']['headline'],
                    'subtitle': g_article['fields']['trailText'],
                    'url_id': g_article['id'],
                    'publish_date': g_article['webPublicationDate']
                })
            search_term_queried = search_term_queried.replace('%20', ' ').replace('"','')
            guardian_articles = orderArticles(guardian_articles, search_term_queried)
            print(search_term_queried)
    except Exception as e:
        print(str(e))
        return str(e)
    

    return json.dumps({'data': [ft_articles, guardian_articles]})

   #https://content.guardianapis.com/search?q=12%20years%20a%20slave&format=json&from-date=2010-01-01&to-date=2010-02-01&show-fields=headline,trailText&order-by=relevance&api-key=25ed0d1e-7578-482c-a15e-4a56a4be88e9 