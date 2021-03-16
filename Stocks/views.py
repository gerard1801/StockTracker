from django.shortcuts import render

import pandas as pd
from yahoofinancials import YahooFinancials

# Create your views here.
def Home(request):
    stock_data = pd.read_csv("/Users/gerardvanderwel/Documents/Stock_data.csv")
    stocks = 1
    stock_price = YahooFinancials("AAPL")
    print(stock_price.get_stock_price_data())

    print(stock_data)
    print(stocks)
    return render(request, 'Stocks.html', {
        'num_stocks': stocks,
    })

def Tracker(request):

    return render(request, 'Tracker.html')