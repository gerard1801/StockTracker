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

    yahoo_data = pull_yahoo_data(stock_tickers)
    #calculate total stock value
    total_stock_value = calculate_port_value(amount_data.tolist(), stock_tickers, yahoo_data)
    #buy price data
    price_data = stock_data.loc[:, "price"].tolist()
    #calculate total buy price
    total_buy_price = buy_price(amount_data.tolist(), price_data)
    #
    total_profit = total_stock_value[0] - total_buy_price

    col_names = stock_data.columns.values

    portfolio_table = table_data(col_names, stock_tickers, amount_data.tolist(), price_data)

    historical_price(stock_tickers)

    return render(request, 'Stocks.html', {
        'portfolio_table':portfolio_table,
        'headers':col_names,
        'stock_tickers':stock_tickers,
        'num_stocks':total_stock_amount,
        'portfolio_value':round(total_stock_value[0], 1),
        'profit':round(total_profit, 1),
        'day_change':round(total_stock_value[1], 1),
    })

def pull_yahoo_data(stock_tickers):
    yahoo_list = []
    for i in stock_tickers:
        yh = YahooFinancials(i)
        yahoo_list.append(yh.get_stock_price_data())
    return yahoo_list

def historical_price(stock_tickers):
    stock_historic_price = YahooFinancials(stock_tickers).get_historical_price_data('2021-03-19', '2021-05-18', 'daily')
    print(stock_historic_price)

def calculate_port_value(amount_data, stock_tickers, yahoo_data):
    stock_value = []
    price_change_list = []
    total_port_value = 0
    day_price_change = 0
    index = 0
    for i in stock_tickers:
        stock_value.append(yahoo_data[index].get(i).get('regularMarketPrice'))
        price_change_list.append(yahoo_data[index].get(i).get('regularMarketChange'))
        index += 1
    for x in range(len(stock_value)):
        total_port_value += stock_value[x] * amount_data[x]
        day_price_change += price_change_list[x] * amount_data[x]
    return [total_port_value, day_price_change]

def buy_price(amount_data, price_data):
    total_buy_price = 0
    for i in range(len(amount_data)):
        total_buy_price += amount_data[i] * price_data[i]
    return total_buy_price

def table_data(col_names, stock_tickers, amount_data, price_data):
    portfolio_table = []
    for i in range(len(stock_tickers)):
        add_list = []
        add_list.append(stock_tickers[i])
        add_list.append(amount_data[i])
        add_list.append(price_data[i])
        portfolio_table.append(add_list)
    return portfolio_table

def Portfolio(request):
    return render(request, 'Portfolio.html')

def Performance(request):
    return render(request, 'Performance.html')

def Dividends(request):
    return render(request, 'Dividends.html')