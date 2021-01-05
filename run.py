from flask import url_for, redirect, render_template, request, abort
from dateutil.relativedelta import relativedelta

from datetime import datetime

from config import app, db, SERVER_NAME
from graph import getGraphElements
from models import stocks, indices
from articles import articleRequestWrapper

@app.route('/')
def index():
    return redirect(SERVER_NAME + '/s/Apple?range=1y&interval=1w&ending=' + datetime.strftime(datetime.now(), '%Y-%m-%d'))

@app.route('/<string:instrument>/<string:commodity>') 
def main(instrument, commodity):
    # get the url params
    time_range_param = request.args.get('range')
    interval_param = request.args.get('interval')
    time_ending_param = request.args.get('ending')
    
    # default url params
    if(not time_range_param): time_range_param = '1y'
    if(not interval_param): interval_param = '1w'
    if(not time_ending_param): time_ending_param = datetime.strftime(datetime.now(), '%Y-%m-%d')
        
    
    # dictionary of dictionary for the args to relativedelta, https://dateutil.readthedocs.io/en/stable/relativedelta.html
    range_array = {
        '3m': {'months' : +3}, 
        '6m': {'months' : +6},
        '1y': {'years' : +1},
        '2y': {'years' : +2},
        '3y': {'years' : +3},
        '5y': {'years' : +5}
    }

    ending_date = datetime.strptime(time_ending_param, '%Y-%m-%d')
    starting_date = ending_date - relativedelta(**range_array[time_range_param])

    date_diff_days = (ending_date - starting_date).total_seconds() / (3600 * 24)

    interval_array = {'1d': 1, '2d': 2, '3d': 3, '1w': 7, '2w': 14, '4w': 28}
    intervals = int(date_diff_days / interval_array[interval_param])

    # get elements from db
    stocks_all = stocks.query.all()
    indices_all = indices.query.all()

    # commodity switch
    if(instrument == 'i'):
        symbol = commodity
        title = indices.query.filter_by(symbol= commodity).first().name
    elif(instrument == 'f'):
        symbol = commodity
        title = commodity
    else:
        symbol = stocks.query.filter_by(url_name= commodity).first().symbol
        title = commodity

    # prepare the graph
    graph = getGraphElements(
        start= starting_date.strftime('%Y-%m-%d'), 
        end= time_ending_param, 
        symbol= symbol,
        title= title
    )

    return render_template('index.html', 
        stocks = stocks_all, 
        indices = indices_all,
        graph_script = graph[0][0],
        graph_div = graph[0][1],
        intervals = intervals,
        y_axis_pixels = graph[1])

@app.route('/articles/', methods=['POST'])
def articles():
    return articleRequestWrapper(request)


if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)