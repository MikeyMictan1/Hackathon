import pandas as pd
import random
from player import Player
import matplotlib.pyplot as plt
from PIL import Image

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
    
IDEALLY the menu has a column showing whether the stock went up/down the day before
little red/green arrows?
'''

class StockMarket:
    def __init__(self):
        self.stocks = None

    def updateCSV(self):
        data = {}
        for stock in self.stocks:
            stockData = [stock.currentPrice, stock.isSafe, stock.numberOwned, stock.wentUp]
            data[stock.name] = stockData
        df = pd.DataFrame(data)
        df.to_csv('StockMarket.csv')
        self.generateImage()

    def readCSV(self):
        df = pd.read_csv('StockMarket.csv')
        self.stocks = []
        for stock in df.columns:
            if stock == 'Unnamed: 0':
                continue
            stockData = df[stock].tolist()
            newStock = Stock(float(stockData[0]), bool(stockData[1]), stock, int(stockData[2]), bool(stockData[3]))
            self.stocks.append(newStock)
        return self.stocks
        # returns list of Stocks (class)

    def updateAllStocks(self):
        for stock in self.stocks:
            stock.updateStock()

    def generateImage(self):
        # Step 1: Read the CSV file
        df = pd.read_csv('stockMarket.csv')
        names = {"Brown's Bakery": ["Brown's Bakery"],
                 'Capital One': ['Capital One'],
                 'Chip NFT': ['Chip NFT'],
                 'Chipdo': ["Chipdo"],
                 }
        dfExtra = pd.DataFrame(names)
        df = pd.concat([dfExtra, df], ignore_index=True)
        df.reset_index()
        df.rename(index={0: 'Stock', 1: 'Price', 2: 'Stability', 3: 'Stocks Owned', 4: 'Went up'}, inplace=True)
        df = df.transpose()
        df.drop('Unnamed: 0', axis=0, inplace=True)

        # Step 2: Create a table using matplotlib
        fig, ax = plt.subplots(figsize=(10, len(df) * 0.4 + 1))  # Adjust the size accordingly
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

        # Adjust the font size and cell dimensions if needed
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 1.5)  # You can adjust the scaling factor

        # Customize the background colors
        # Set background color for header row
        header_color = '#769974'  # Light gray for the header
        for i, col in enumerate(df.columns):
            table[0, i].set_facecolor(header_color)

        # Set background color for all cells
        cell_color = '#a7cca5'  # Light background for cells
        for row in range(1, len(df) + 1):
            for col in range(len(df.columns)):
                table[row, col].set_facecolor(cell_color)

        # Save the table as an image
        plt.savefig('stockMarket.png', bbox_inches='tight', dpi=300, transparent=True)

class Stock:
    def __init__(self, currentPrice, isSafe, stockName, numberOwned, wentUp):
        self.name = stockName
        self.currentPrice = currentPrice
        self.isSafe = isSafe
        self.numberOwned = numberOwned # number of stocks actually owned
        self.wentUp = wentUp

    def buyStock(self, numOfStocks, playerObject, stockMarketObject):
        amountToSpend = self.currentPrice*numOfStocks
        if amountToSpend > playerObject.loadBalance():
            print("You don't have enough!")
        else:
            self.numberOwned += numOfStocks
            playerObject.updateBalance(round(-amountToSpend, 2))
        stockMarketObject.updateCSV()

        # FOR NOW!!!
        stockMarketObject.updateAllStocks()

    def sellStock(self, numOfStocks, playerObject, stockMarketObject):
        self.numberOwned -= numOfStocks
        playerObject.updateBalance(round(self.currentPrice * numOfStocks, 2))
        stockMarketObject.updateCSV()

        # FOR NOW!!!
        stockMarketObject.updateAllStocks()

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
            self.wentUp = True
            self.currentPrice = self.currentPrice * (1 + (percentageChange / 100))
            self.currentPrice = round(self.currentPrice, 2)
        else:
            self.wentUp = False
            self.currentPrice = self.currentPrice * (1 - (percentageChange / 100))
            self.currentPrice = round(self.currentPrice, 2)


stockMarket = StockMarket()
stockMarket.readCSV()
stockMarket.updateAllStocks()
stockMarket.updateCSV()
stocks = stockMarket.readCSV()

test = Player()
print(test.currentBalance)
stocks[0].buyStock(1, test)
print(stocks[0].numberOwned)
print(test.currentBalance)
