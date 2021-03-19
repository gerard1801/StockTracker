from django.shortcuts import render

import pandas as pd
from yahoofinancials import YahooFinancials

# Create your views here.
def Home(request):
    #Stock data
    stock_data = pd.read_csv("/Users/gerardvanderwel/Documents/Stock_data.csv", sep=';')

    #extract and calculate total amount of stocks
    amount_data = stock_data.loc[:, "amount"]
    total_stock_amount = amount_data.sum()

    stock_price = YahooFinancials("AAPL")
    print(stock_price.get_stock_price_data())
    return render(request, 'Stocks.html', {
        'num_stocks':total_stock_amount,
    })

def Tracker(request):

    return render(request, 'Tracker.html')