from datetime import datetime
import os

class Player:
    def __init__(self):
        self.weeklySalary = 100
        self.prevMonth, self.prevWeek = self.load_prev_month_week()
        self.today = datetime.now()
        self.week = (self.today.strftime("%V")) #Week number via string eg 42 or 01
        self.month = int(self.today.strftime("%m")) #Month number via int eg 11

        self.currentBalance = self.load_balance() #Loading in the balance

    #Storing balance system
    def load_balance(self):
        if os.path.exists('balance.txt'):
            with open('balance.txt', 'r') as f:
                return float(f.read().strip())
        else:
            return 100

    def update_balance(self, amount):
        self.currentBalance += amount
        self.save_balance()

    #Comparing the previous month/week status to the current to check if the week/month has changed
    def load_prev_month_week(self):
        if os.path.exists('prev_month_week.txt'):
            with open('prev_month_week.txt', 'r') as f:
                prev_month, prev_week = f.read().strip().split(',')
                return int(prev_month), prev_week.strip()
        else:
            return 1, '1'

    #Saving data
    def save_balance(self):
        with open('balance.txt', 'w') as f:
            f.write(str(self.currentBalance))

    #Saving data
    def save_prev_month_week(self):
        with open('prev_month_week.txt', 'w') as f:
            f.write(f"{self.month},{self.week}")

    #Changes bank account balance
    def bankAccount(self):
        if self.week != self.prevWeek:
            self.currentBalance += self.weeklySalary

        if self.month != self.prevMonth:
            self.currentBalance *= 1.025

        if self.month != self.prevMonth or self.week != self.prevWeek:
            self.prevMonth = self.month
            self.prevWeek = self.week

        print("Current Balance: ", int(self.currentBalance))

        self.save_balance()
        self.save_prev_month_week()



test = Player()
test.bankAccount()


    #2.5% interest per year Capital one
