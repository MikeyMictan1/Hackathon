import pandas as pd
import random

'''
TO USE:
stockMarket = StockMarket()
stockMarket.readCSV() <-- reads current
stockMarket.updateAllStocks() <-- runs stock 'simulation'
stockMarket.updateCSV() <-- updates csv file

can get stock info like this:
stocks = stockMarket.readCVS()
for stock in stocks:
    price = stock.currentPrice
    safety = stock.isSafe
    name = stock.name
'''

class StockMarket:
    def __init__(self):
        self.stocks = None

    def updateCSV(self):
        data = {}
        for stock in self.stocks:
            stockData = [stock.currentPrice, stock.safeStock]
            data[stock.name] = stockData
        df = pd.DataFrame(data)
        df.to_csv('StockMarket.csv')

    def readCSV(self):
        df = pd.read_csv('StockMarket.csv')
        self.stocks = []
        for stock in df.columns:
            if stock == 'Unnamed: 0':
                continue
            stockData = df[stock].tolist()
            newStock = Stock(float(stockData[0]), bool(stockData[1]), stock)
            self.stocks.append(newStock)
        return self.stocks
        # returns list of Stocks (class)

    def updateAllStocks(self):
        for stock in self.stocks:
            stock.updateStock()

class Stock:
    def __init__(self, currentPrice, isSafe, stockName):
        self.name = stockName
        self.currentPrice = currentPrice
        self.isSafe = isSafe

    def updateStock(self):
        if self.isSafe == True:
            safetyVar = 4
            perVar = 6
        else:
            safetyVar = 11
            perVar = 11

        upOrDown = random.randrange(1, safetyVar)
        percentageChange = random.randrange(1, perVar)
        if upOrDown == 1:
            self.currentPrice = self.currentPrice * (1 + (percentageChange / 100))
            self.currentPrice = round(self.currentPrice, 2)
        else:
            self.currentPrice = self.currentPrice * (1 - (percentageChange / 100))
            self.currentPrice = round(self.currentPrice, 2)


stockMarket = StockMarket()
stockMarket.readCSV()
stockMarket.updateAllStocks()
stockMarket.updateCSV()
stocks = stockMarket.readCSV()
