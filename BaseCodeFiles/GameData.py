import datetime
import pandas as pd

# all functions in this order vvv
# petHappiness petHunger petThirst playerMoney playerSavingsAccount lastTimeRecorded ownedItems

class GameData:
    def __init__(self):
        self.petHappiness = 0
        self.petHunger = 0
        self.petThirst = 0
        self.ownedItems = []
        self.playerMoney = 100
        self.playerSavingsAccount = 0 # amount of money in savings, Null if no savings
        self.lastTimeRecorded = []

    def getCurrentTime(self):
        currentTime = str(datetime.datetime.now())
        outTime = currentTime[:10]
        outTime = outTime + "-" + currentTime[11:13]
        outTime = outTime + "-" + currentTime[14:16]
        outTime = outTime + "-" + currentTime[17:]
        return outTime

    def setGameData(self, happiness, hunger, thirst, savingsAccount, money, ownedItems):
        self.lastTimeRecorded = self.getCurrentTime()
        data = {
            'petHappiness': [happiness],
            'petHunger': [hunger],
            'petThirst': [thirst],
            'playerMoney': [money],
            'playerSavingsAccount': [savingsAccount],
            'lastTimeRecorded': [self.lastTimeRecorded],
        }
        extraData = {
            'ownedItems': ownedItems,
        }
        df = pd.DataFrame(data)
        df2 = pd.DataFrame(extraData)
        finaldf = pd.concat([df, df2], axis=1)
        print(finaldf)
        finaldf.to_csv("gameData.csv", header=True)

    def getGameData(self):
        df = pd.read_csv('gameData.csv')
        self.petHappiness = int(df.loc[0, 'petHappiness'])
        self.petHunger = int(df.loc[0, 'petHunger'])
        self.petThirst = int(df.loc[0, 'petThirst'])
        self.playerMoney = float(df.loc[0, 'playerMoney'])
        self.playerSavingsAccount = float(df.loc[0, 'playerSavingsAccount'])
        self.lastTimeRecorded = df.loc[0, 'lastTimeRecorded']
        self.ownedItems = df['ownedItems'].tolist()

        return self.petHappiness, self.petHunger, self.petThirst, self.playerMoney, self.playerSavingsAccount, self.lastTimeRecorded, self.ownedItems



test = GameData()
test.setGameData(100,100,100,0,0,[0,0])
print(test.getGameData())
