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
        self.__screen = pygame.display.get_surface()

        # hud infos
        self.__controls_font = pygame.font.Font("../Fonts/Pixel.ttf", 30)
        self.general_font = pygame.font.Font("../Fonts/Primer.otf", 40)

        # animations
        self.__frame = 0
        self.__frame_speed = 0.1
        self.__animation_dict = {"idle": []}
        self.__animation_dict = gf.import_graphics_dict("pet", self.__animation_dict, "../Graphics")
        self.__state = "idle"
        self.image = self.__animation_dict[self.__state][self.__frame]
        self.image = pygame.transform.scale(self.image, (self.__rect_width, self.__rect_height))
        self.rect = self.image.get_rect(topleft=pos)
        # mikey pygame changes ---
    #
        self.dead = False
        self.name = "chip"
        self.maxHunger,self.hunger = 100,100#hunger
        self.maxHappiness, self.happiness = 100,100#happiness
        self.maxThirst, self.thirst = 100,100#thirsty
        self.highenough = 80
        self.tooLow = 20
        self.happinessTick = -2
        self.hungerTick = -3
        self.thirstTick = -1
    #
    #increments hunger by a certain amount
    def changeHunger(self, hungerChange ):
    #
        self.hunger = self.hunger +  hungerChange
        if(hungerChange != 0):
            print (hungerChange,self.maxHunger)
    #
    def changeHappiness(self, happinessChange ):
    #
        self.happiness += happinessChange
    #
    def changeThirst(self, thirstChange ):
    #
        self.thirst += thirstChange
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
        if self.hunger <= 0 or self.happiness <= 0 or self.thirst <= 0:
            return True

        else:
            return False



    def updatePet(self,numhours):
    #
        print(numhours * self.hungerTick,"this is going to be a negative number")
        self.changeHunger(self.hungerTick * numhours)
        self.changeThirst(self.thirstTick * numhours)
        self.updateHappiness(numhours)
        if(numhours != 0):
        #
            print ("numhours is now",numhours)
            print(numhours * self.hungerTick, "this is going to be a negative number")
            print(self.hunger, self.happiness,"thirst is",self.thirst)
        #
    #
    # MIKEY PYGAME STUFF GO AWAY ADRIAN EWW C-CODER--------
    def update(self):
        self.hud()
        self.animation()

    def hud(self):
        self.happiness_text = self.general_font.render(f"Happiness: {self.happiness}", True, (255,255,255))
        self.__screen.blit(self.happiness_text,(gf.screen_width // 15, gf.screen_height // 10))

        self.hunger_text = self.general_font.render(f"Hunger:     {self.hunger}", True, (255,255,255))
        self.__screen.blit(self.hunger_text,(gf.screen_width // 15, gf.screen_height // 20))

        self.thirst_text= self.general_font.render(f"Thirst:       {self.thirst}", True, (255,255,255))
        self.__screen.blit(self.thirst_text,(gf.screen_width // 15, gf.screen_height // 6.5))

        self.home_text = gf.smaller_title_font.render(f"Chip's Humble Abode", True, (255, 255, 255))
        self.__screen.blit(self.home_text, (gf.img_centre(self.home_text)[0], gf.screen_height // 20))

    def animation(self):
        self.__frame += self.__frame_speed
        if self.__frame >= len(self.__animation_dict["idle"]):  # could be any folder, but took the first one
            self.__frame = 0

        self.image = self.__animation_dict[self.__state][int(self.__frame)]
        self.image = pygame.transform.scale(self.image, (self.__rect_width, self.__rect_height))

'''test = Pet()
test.changeHunger(-22)
print(test.hunger, " is hunger")
test.updatePet(3)
print(test.happiness)
print(test.hunger, " is hunger 2")'''
