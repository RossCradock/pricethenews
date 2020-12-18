
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from datetime import datetime
import json

from config import FT_API_KEY, GUARDIAN_API_KEY

request_json = {'start': '27-09-2020', 'end': '30-09-2020', 'tags': ['MSFT', 'computer chip']}
print(request_json)
start_date = datetime.strptime(request_json['start'], '%d-%m-%Y')
end_date = datetime.strptime(request_json['end'], '%d-%m-%Y')

tags = request_json['tags']
tags_map = map(lambda tag: tag + ' AND ', tags)
tags_string = ''.join(list(tags_map))

# Financial times
url = 'https://api.ft.com/content/search/v1?'
headers = {
    'Content-Type': 'application/json',
    'X-Api-Key': FT_API_KEY,
}

query_string = (
    tags_string 
    + 'lastPublishDateTime:>' 
    + start_date.strftime('%Y-%m-%dT00:00:00Z') + ' AND '
    + 'lastPublishDateTime:<' 
    + end_date.strftime('%Y-%m-%dT00:00:00Z')
)
body = {
    'queryString': query_string,
    'resultContext': {
        'aspects': 
        ['title', 'lifecycle', 'location','summary', 'editorial']
    }
}
"""         'curations': [
            'ARTICLES',
            'BLOGS',
            'PAGES',
        ], """
encoded_body = json.dumps(body).encode('utf-8')
print(encoded_body)
#exit()
try:
    ft_request = Request(url, encoded_body, headers)
    with urlopen(ft_request) as f:
        ft_result = f.read()
    print(ft_result.decode())
except Exception as e:
    print(e)