from datetime import datetime, timedelta


class SavingsAcc():
#
    def __init__(self,endDate,moneyIn):
    #
        #self.startDate = startDate
        self.endTime = endDate
        self.interestNum = 1.025
        self.interestVal = 2.5
        self.money = moneyIn
    #
    #given what time it is, can the user retrieve their money
    def isDone (self,currentTime):
    #
        if( self.endTime - currentTime <= timedelta(0)):
        #
            return True
        #
        return False
    #
    #if the waiting time is over it will return the new money earned
    def getMoney(self,currentTime):
    #
        if(self.isDone(currentTime)):
        #
            result = self.money * self.interestNum
            return result
        #
    #
    def timeLeft(self,currentTime):
    #
        difference = self.endTime - currentTime
        if(difference > timedelta(0)):
        #
            return difference
        #
        return timedelta(0)
    #
#