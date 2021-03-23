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
    #extract all stock tickers
    stock_tickers = stock_data.loc[:, "stock"].tolist()
    #calculate total stock value
    total_stock_value = calculate_port_value(amount_data.tolist(), stock_tickers)
    #buy price data
    price_data = stock_data.loc[:, "price"]
    #calculate total buy price
    total_buy_price = buy_price(amount_data.tolist(), price_data.tolist())
    #
    total_profit = total_stock_value - total_buy_price
    #
    price_change_day = day_change(amount_data, stock_tickers)

    return render(request, 'Stocks.html', {
        'num_stocks':total_stock_amount,
        'portfolio_value':round(total_stock_value, 1),
        'profit':round(total_profit, 1),
        'day_change':round(price_change_day, 1),
    })

def calculate_port_value(amount_data, stock_tickers):
    stock_value = []
    total_port_value = 0
    for i in stock_tickers:
        price_dict = YahooFinancials(i).get_stock_price_data()
        price = price_dict.get(i).get('regularMarketPrice')
        stock_value.append(price)
    for x in range(len(stock_value)):
        total_port_value += stock_value[x] * amount_data[x]
    return total_port_value

def buy_price(amount_data, price_data):
    total_buy_price = 0
    for i in range(len(amount_data)):
        total_buy_price += amount_data[i] * price_data[i]
    return total_buy_price

def day_change(amount_data, stock_tickers):
    day_price_change = 0
    price_change_list = []
    for i in stock_tickers:
        price_data = YahooFinancials(i).get_stock_price_data()
        price_change = price_data.get(i).get('regularMarketChange')
        price_change_list.append(price_change)
    for x in range(len(price_change_list)):
        day_price_change += price_change_list[x] * amount_data[x]
    return day_price_change


def Tracker(request):

    return render(request, 'Tracker.html')