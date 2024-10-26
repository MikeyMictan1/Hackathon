import math
from datetime import datetime
# a test
# irene is here!!!!!!!!!!
'''PROPER COMMENTING AAAAAAAA'''
# adrian !!!!
# this is a pull

print('THIS IS CRYSTAL DOES THIS WORK')
#testinggg

'''yo'''
print("This is crystal's actual laptop.")

# CRYSTAL DO YOU SEE THIS??????
# YES :DD
time1 = datetime(2024,10,26,12,34)
time2 = datetime(2024,10,26,14,32)
def compareTime(lastTimeCheck,currentTime):
    #
    #currentTime = datetime.now()
    difference = currentTime - lastTimeCheck
    diffHours = (difference.total_seconds() / 3600)
    print(diffHours)
    if diffHours > 1:
    #
        lastTimeCheck = currentTime
        return int(diffHours)
    #
    return 0
#
print(compareTime(time1,time2),"is the diff in hours")

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
# mikey pygame changes ---