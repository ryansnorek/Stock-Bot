import requests
import json
from stockSymbols import other

# Requires a TD Ameritrade account with API access
td_consumer_key = 'MY_TD_CONSUMER_KEY'

symbols = other


def getStockData(symbol):
    endpoint = f'https://api.tdameritrade.com/v1/marketdata/{symbol}/quotes'
    page = requests.get(url=endpoint, params={'apikey': td_consumer_key})
    content = json.loads(page.content)

    stock = content[symbol]

    stockData = {
        'name': stock['description'],
        'symbol': stock['symbol'],
        'price': stock['mark'],
        'dividend': stock['divAmount'],
        'dividendYield': stock['divYield'],
        'peRatio': stock['peRatio'],
        # 'NAV': stock['nAV'],
        # 'volume': stock['totalVolume'],
    }

    return stockData


def getFundamentalData(symbol):
    endpoint = f'https://api.tdameritrade.com/v1/instruments'
    page = requests.get(url=endpoint, params={
        'apikey': td_consumer_key,
        'symbol': symbol,
        'projection': 'fundamental'
    })
    content = json.loads(page.content)

    stock = content[symbol]['fundamental']

    fundamentalData = {
        # 'divGrowthRate3Year': stock['divGrowthRate3Year'],
        'pegRatio': stock['pegRatio'],
        'eps': stock['epsTTM'],
        # 'returnOnInvestment': stock['returnOnInvestment']
    }

    return fundamentalData


def grahamLynchModel(stockData):
    eps = stockData['eps']
    price = stockData['price']
    corporateAAABondYield = 0.04

    # Fair Value = EPS * (8.5 + 2G)
    fairValue = round(
        (eps * (8.5 + 2 * (longTermGrowthRate * 100))), 2)

    adjustedFairValue = round(
        fairValue * (4.4 / (corporateAAABondYield * 100)), 2)

    change = round(((price - adjustedFairValue) / price) * 100)

    valued = 'Undervalued'
    if (change > 0):
        valued = 'Overvalued'

    stockData['fairValue'] = adjustedFairValue
    stockData['change'] = change
    stockData['valued'] = valued
    stockData['growthRate'] = round(longTermGrowthRate, 2)


def printReport():
    name = stockData['name']
    price = stockData['price']
    dividend = stockData['dividend']
    fairValue = stockData['fairValue']
    valued = stockData['valued']
    change = stockData['change']
    growthRate = stockData['growthRate']
    peRatio = stockData['peRatio']
    earningsGrowthRate = round(stockData['earningsGrowth'], 2)

    print(symbol)
    print(name)
    print('Dividend Yield: ', dividend, '%')
    print("Current Price: $", price)
    print("Fair Value: $", fairValue)
    print('Earnings Growth Rate: ', earningsGrowthRate)
    print('Long Term Growth Rate: ', growthRate)
    print('PE Ratio: ', peRatio)
    print(valued, change, '%')
    print()
    print(stockData['eps'])


for symbol in symbols:
    stockData = getStockData(symbol)
    fundamentalData = getFundamentalData(symbol)
    stockData.update(fundamentalData)
    if (stockData['peRatio'] != 0 and stockData['pegRatio'] != 0):

        earningsGrowthRate = (
            stockData['peRatio'] / stockData['pegRatio']) / 100

        stockData['earningsGrowth'] = earningsGrowthRate
        longTermGrowthRate = 0.1

        grahamLynchModel(stockData)
        printReport()
