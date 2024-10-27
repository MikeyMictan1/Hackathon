from datetime import datetime
import os
from dataExtractor import DataHandler

class Player:
    def __init__(self):
        self.dataHandler = DataHandler()
        self.weeklySalary = 100
        self.inflation = 1.0175
        self.bankInterest = 1.015
        self.prevMonth, self.prevWeek = self.loadPrevMonthWeek()
        self.today = datetime.now()
        self.week = (self.today.strftime("%V")) #Week number via string eg 42 or 01
        self.month = int(self.today.strftime("%m")) #Month number via int eg 11

        self.currentBalance = float(self.dataHandler.read_value('currentBalance'))
        self.currentRent = float(self.dataHandler.read_value('currentRent'))
        # savings
        self.savings_balance = float(self.dataHandler.read_value('currentRent'))
        self.savingAccountOpen = False # CHANGE TO READ FILE
        self.savingAccountDate = None # CHANGE TO READ FILE

    def updateBalance(self, amount):
        self.currentBalance += amount
        self.saveBalance()

    def loadRent(self):
        if os.path.exists('rent.txt'):
            with open('rent.txt', 'r') as f:
                return float(f.read().strip())
        else:
            return 40

    def updateRent(self):
        self.currentRent *= self.inflation
        self.saveRent()

    #Comparing the previous month/week status to the current to check if the week/month has changed
    def loadPrevMonthWeek(self):
        if os.path.exists('prev_month_week.txt'):
            with open('prev_month_week.txt', 'r') as f:
                prevMonth, prevWeek = f.read().strip().split(',')
                return int(prevMonth), prevWeek.strip()
        else:
            return 1, '1'

    #Saving data
    def saveBalance(self):
        self.dataHandler.replace_value('currentBalance', self.currentBalance)

    def saveRent(self):
        self.dataHandler.replace_value('currentRent', self.currentRent)


    #Saving data
    def savePrevMonthWeek(self):
        with open('prev_month_week.txt', 'w') as f:
            f.write(f"{self.month},{self.week}")

    #Changes bank account balance
    def bankAccount(self):
        if self.week != self.prevWeek:
            self.currentBalance += self.weeklySalary

        if self.month != self.prevMonth:
            self.currentBalance *= self.bankInterest
            self.currentRent *= self.inflation
            self.currentBalance -= self.currentRent

        if self.month != self.prevMonth or self.week != self.prevWeek:
            self.prevMonth = self.month
            self.prevWeek = self.week

        print("Current Balance: ", self.currentBalance)

        self.saveBalance()
        self.saveRent()
        self.savePrevMonthWeek()



test = Player()
test.bankAccount()


    #2.5% interest per year Capital one
