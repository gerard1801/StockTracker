from django.shortcuts import render

import pandas as pd
from yahoofinancials import YahooFinancials

# Create your views here.
def Home(request):
    stock_data = pd.read_csv("/Users/gerardvanderwel/Documents/Stock_data.csv")
    stock_price = YahooFinancials("AAPL")
    print(stock_price.get_stock_price_data())

    print(stock_data)
    #print(stock_data)
    return render(request, 'Stocks.html')