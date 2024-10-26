import pygame
import datetime
'''the things the pet should be able to do and the stats it should have:
hunger, happiness, thirst

'''

class Pet:
#
    def __init__(self):
    #
        self.dead = False
        self.name = "chip"
        self.maxHunger,self.hunger = 100,100
        self.maxHappiness, self.happiness = 100,100
        self.maxThirst, self.thirst = 100,100
        self.highenough = 80
        self.tooLow = 20
        self.happinessTick = -4
    #
    #increments hunger by a certain amount
    def changeHunger(self, hungerChange ):
    #
        self.maxHunger += hungerChange
    #
    def changeHappiness(self, happinessChange ):
    #
        self.maxHappiness += happinessChange
    #
    def changeThirst(self, thirstChange ):
    #
        self.maxThirst += thirstChange
    #
    def interestHappiness(self, happinessInterest ):
    #
        self.maxHappiness *= happinessInterest
    #
    def getname(self):
    #
        return self.name
    #
    def updateHappiness(self,numHours):
    #
        flagBad = False
        flagGood = False
        if(self.hunger <= self.tooLow):
        #
            flagBad = True
        #
        if(self.hunger >= self.highenough):
        #
            flagGood = True
        #
        if(self.thirst <= self.tooLow):
        #
            flagBad = True
        #
        if(self.thirst >= self.highenough):
        #
            flagGood = True
        #
        if(flagBad):
        #
            self.changeHappiness(self.happinessTick *numHours)
        #
        elif(flagGood):
        #
            self.changeHappiness(self.happinessTick *-1 *numHours)
            if(self.happiness > self.maxHappiness):
            #
                self.happiness = self.maxHappiness
            #
        #
    #
    def checkDead(self):
    #
        if(self.hunger <= 0 or self.happiness <= 0 or self.thirst <= 0):
        #
            dead = True
        #
    #
#

test = Pet()
test.changeHunger(-22)
print(test.hunger, " is hunger")
test.updateHappiness(3)
print(test.happiness)
