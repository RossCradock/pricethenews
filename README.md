# pricethenews
[website](https://pricethenews.com)


_Website to view the price of stocks, indices and currencies along with the news articles that change them_

Articles retrieved from FT.com and The Guardian's open-source APIs. 
Both these APIs allow for 5000 requests per day with rate limiting per second as well. For this reason the website cannot scale.
The guardian T&Cs mentions that there is no advertising allowed. FT.com has no stipulations.

Search is optimised to show most relevant results first with a system to retreive broader and broader results 
i.e. if you search for AirBnB it will search for 'airbnb' first then it will search for 'gig economy' and finally 'real estate' so that it will always show some articles.
This is unless a user enters a specific search term.

Price data is displayed for 12 currency exchanges, 85 company stocks and 30 indices. 
Library [yfinance](https://github.com/ranaroussi/yfinance) is used for the stocks and indices pricing.
https://exchangeratesapi.io/ is used for the forex figures which aggregates them from the european central bank api into time-series data.
Once the data is retreived it is put into pandas dataframes which is then used with a bokeh graph.
  
The interval picker includes allowed date ranges from 10 years ago and the intervals that can be used.
The calendar is a bootstrap date-picker.

## Technologies and versions:
### Backend
- Python 3.7.7
- Flask 1.1.2
- SQLAlchemy 2.4.4
- SQLite 3.32.3
- NumPy 1.19.4
- Pandas 1.1.4
- Bokeh 2.2.3
- yfinance 0.1.55

### Frontend
- Javascript
- HTML5
- CSS3
- Bootstrap 3.4.1
- JQuery 3.5.1



