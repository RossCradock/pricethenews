import numpy 
import pandas as pd
import yfinance
import math

from bokeh.plotting import figure, show
from bokeh.embed import components

def findPaddingLeftPixels(price_close):
    y_axis_pixels = 28
    contains_decimal = numpy.nanmax(price_close) - numpy.nanmin(price_close) < 4
    digits = math.floor(math.log10(numpy.nanmax(price_close))) + 1
    if digits > 5:
        return 84
    if contains_decimal:
        y_axis_pixels += 2 if digits > 2 else 3
        digits += 1
    
    return y_axis_pixels + (8 * digits)

def getGraphElements(start, end, symbol, title):
    # retrieve data from yfinance
    price_data = yfinance.Ticker(symbol).history(
        interval = '1d',
        start = start, 
        end = end,
        prepost = True,
        actions = False
    )

    try:
        # make the date index a column, unset the timezone
        price_data['Date'] = price_data.index.tz_localize(None) 
    except AttributeError:
        # for indices without dates
        price_data['Date'] = price_data.index

    # create a new plot with a datetime axis type
    plot = figure(
        plot_width=800, 
        plot_height=500, 
        x_axis_type="datetime", 
        toolbar_location=None
    )

    price_close = numpy.array(price_data['Close'])
    price_close_dates = numpy.array(price_data['Date'], dtype=numpy.datetime64)

    # add renderers
    plot.line(price_close_dates, price_close, color='navy')
    
    # make sure Nan's show at start - https://stackoverflow.com/questions/65042319/bokeh-graph-starting-or-finishing-with-nan-y-axis-values-is-not-shown/65044129#65044129
    plot.x_range.start = min(price_close_dates) 
    plot.x_range.end = max(price_close_dates)

    # find out the price digits to change the interval picker padding
    y_axis_pixels = findPaddingLeftPixels(price_close)

    # customize by setting attributes
    plot.title.text = title
    plot.grid.grid_line_alpha = 0.1
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = 'Price($)'
    plot.ygrid.band_fill_color = 'lightblue'
    plot.ygrid.band_fill_alpha = 0.3
    plot.sizing_mode = 'stretch_width'

    return [components(plot), y_axis_pixels]