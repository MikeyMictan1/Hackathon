import pygame
import datetime
import globalfunctions as gf
'''the things the pet should be able to do and the stats it should have:
hunger, happiness, thirst

'''

class Pet(pygame.sprite.Sprite):
#
    def __init__(self, pos, groups, wall_sprites):
        # mikey pygame changes ---
        super().__init__(groups)
        self.__wall_sprites = wall_sprites
        self.__position = pos
        self.__rect_width = 200
        self.__rect_height = 200
        self.__character_width = 200
        self.__character_height = 160
        self.__screen = pygame.display.get_surface()
        self.image = pygame.image.load('../Graphics/pet/pet.png')
        self.image = pygame.transform.scale(self.image, (self.__rect_width, self.__rect_height))
        self.rect = self.image.get_rect(topleft=pos)

        # hud infos
        self.__controls_font = pygame.font.Font("../Fonts/Pixel.ttf", 30)

        # mikey pygame changes ---
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

    def updatePet(self,numhours):
    #
        a =0
    #
    # MIKEY PYGAME STUFF GO AWAY ADRIAN EWW C-CODER--------
    def update(self):
        self.hud()

    def hud(self):
        self.happiness_text = self.__controls_font.render(f"Happiness: {self.happiness}", True, (255,255,255))
        self.__screen.blit(self.happiness_text,(gf.screen_width // 15, gf.screen_height // 10))

        self.hunger_text = self.__controls_font.render(f"Hunger: {self.hunger}", True, (255,255,255))
        self.__screen.blit(self.hunger_text,(gf.screen_width // 15, gf.screen_height // 20))

        self.thirst_text= self.__controls_font.render(f"Thirst: {self.thirst}", True, (255,255,255))
        self.__screen.blit(self.thirst_text,(gf.screen_width // 15, gf.screen_height // 6.5))


#test = Pet()
#test.changeHunger(-22)
#print(test.hunger, " is hunger")
#test.updateHappiness(3)
#print(test.happiness)
