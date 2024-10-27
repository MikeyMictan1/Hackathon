import pygame
import globalfunctions as gf
from dataExtractor import DataHandler
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
        self.__rect_width = 150
        self.__rect_height = 250
        self.__screen = pygame.display.get_surface()
        self.outfitted = False
        self.data = DataHandler()

        # hud infos
        self.__controls_font = pygame.font.Font("../Fonts/Pixel.ttf", 30)
        self.general_font = pygame.font.Font("../Fonts/Primer.otf", 40)

        # animations
        self.__frame = 0
        self.__frame_speed = 0.1
        self.__animation_dict = {"idle": [], "outfit":[]}
        self.__animation_dict = gf.import_graphics_dict("pet", self.__animation_dict, "../Graphics")
        self.__state = "idle"
        self.image = self.__animation_dict[self.__state][self.__frame]
        self.image = pygame.transform.scale(self.image, (self.__rect_width, self.__rect_height))
        self.rect = self.image.get_rect(topleft=pos)

        self.chips_abode_img = pygame.image.load("../Graphics/pet/chips_abode.png")
        self.chips_abode_img = pygame.transform.scale(self.chips_abode_img, (350,300))

        self.controls_img = pygame.image.load("../Graphics/pet/controls.png")
        self.controls_img = pygame.transform.scale(self.controls_img, (300,200))

        self.windows_img = pygame.image.load("../Graphics/pet/windows.png")
        self.windows_img = pygame.transform.scale(self.windows_img, (600,800))

        self.food_img = pygame.image.load("../Graphics/pet/food.png")
        self.food_img = pygame.transform.scale(self.food_img, (40, 40))

        self.happiness_img = pygame.image.load("../Graphics/pet/happiness.PNG")
        self.happiness_img = pygame.transform.scale(self.happiness_img, (40, 40))

        self.thirst_img = pygame.image.load("../Graphics/pet/thirst.png")
        self.thirst_img = pygame.transform.scale(self.thirst_img, (40, 40))

        self.rand_decor_img = pygame.image.load("../Graphics/pet/rand_decor.PNG")
        self.rand_decor_img = pygame.transform.scale(self.rand_decor_img, (150, 200))
    #
        self.dead = False
        self.name = "chip"
        self.maxHunger,self.hunger = 100,int(self.data.read_value('hungerLevel'))#hunger
        self.maxHappiness, self.happiness = 100,int(self.data.read_value('happinessLevel'))#happiness
        self.maxThirst, self.thirst = 100,int(self.data.read_value('thirstLevel'))#thirsty
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

        if (self.hunger > self.maxHunger):
        #
            self.hunger = self.maxHunger
        self.data.replace_value('hungerLevel', self.hunger)
        #
    #
    def setstats(self,petHappiness, petHunger, petThirst):
    #
        self.happiness = petHappiness
        self.hunger = petHunger
        self.thirst = petThirst
    #
    def changeHappiness(self, happinessChange ):
    #
        self.happiness -= happinessChange
        self.data.replace_value('happinessLevel', self.happiness)


    #
    def setMax(self):
    #
        if (self.happiness > self.maxHappiness):
        #
            self.happiness = self.maxHappiness
        #
        if (self.hunger > self.maxHunger):
        #
            print(self.maxHunger,"is new max hunger")
            self.hunger = self.maxHunger
        #
        if (self.thirst > self.maxThirst):
        #
            self.thirst = self.maxThirst
        #

    #
    def changeThirst(self, thirstChange ):
    #
        self.thirst += thirstChange
        if (self.thirst > self.maxThirst):
        #
            self.thirst = self.maxThirst
        self.data.replace_value('thirstLevel', self.thirst)
        #
    #
    def interestHappiness(self, happinessInterest ):
    #
        self.maxHappiness *= happinessInterest
        if (self.happiness > self.maxHappiness):
        #
            self.happiness = self.maxHappiness
        #
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

    def updatePet(self,numhours):
    #
        self.changeHunger(self.hungerTick * numhours)
        self.changeThirst(self.thirstTick * numhours)
        self.updateHappiness(numhours)

        #
    #

    def resetStats(self):
        self.data.replace_value('hungerLevel', 100)
        self.data.replace_value('happinessLevel', 100)
        self.data.replace_value('thirstLevel', 100)
        self.data.replace_value('currentBalance', 100)
        self.data.replace_value('currentRent', 40)
        self.data.replace_value('savingsBalance', 50)

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

        self.__screen.blit(self.windows_img, (gf.img_centre(self.windows_img)[0], gf.img_centre(self.windows_img)[1]))
        self.__screen.blit(self.chips_abode_img, (gf.img_centre(self.chips_abode_img)[0], 0))
        self.__screen.blit(self.controls_img, (0, gf.screen_height // 1.4))
        self.__screen.blit(self.food_img, (gf.screen_width // 30, gf.screen_height // 20))
        self.__screen.blit(self.happiness_img, (gf.screen_width // 30, gf.screen_height // 10))
        self.__screen.blit(self.thirst_img, (gf.screen_width // 30, gf.screen_height // 6.5))
        self.__screen.blit(self.rand_decor_img, (gf.screen_width // 15, gf.screen_height //2.5))

    def animation(self):
        self.__frame += self.__frame_speed
        if self.__frame >= len(self.__animation_dict["idle"]):  # could be any folder, but took the first one
            self.__frame = 0

        if self.outfitted:
            self.__state = "outfit"
        else:
            self.__state = "idle"

        self.image = self.__animation_dict[self.__state][int(self.__frame)]
        self.image = pygame.transform.scale(self.image, (self.__rect_width, self.__rect_height))
