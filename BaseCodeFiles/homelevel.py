import pygame
import GameData as GameData
import homelayout as mz_lay
import globalfunctions as gf
import camera as cam
import pet as pet
from datetime import datetime
import csv, os
import player as pl
import RandomEvents as Events


class HomeLevel:
    def __init__(self, layout_list: list):
        # sprite groups setup
        self.__wall_sprites = pygame.sprite.Group()
        self.__game_camera = cam.GameCamera()
        self.lastTimeCheck = datetime.now() # change this later becuase it should be initialised to what is in the file if there is one
        self.lastTimeCheckHours = datetime.now()# also need to change this later to time saved in file
        self.player = pl.Player()
        # maze creation
        self.create_pygame_home(layout_list)
        #self.Events = Events.Event()
        # other setup
        self.is_active = True
        self.level_type = "normal"
        self.gameData = GameData.GameData()
        self.petHappiness, self.petHunger, self.petThirst, self.playerMoney, self.playerSavingsAccount, self.lastTimeRecorded, self.ownedItems = self.gameData.getGameData()
        self.numbers_list = [float(num) for num in self.lastTimeRecorded.split('-')]
        self.numbers_list = [int(num) for num in self.numbers_list]
        self.lastTimeRecorded = datetime(self.numbers_list[0], self.numbers_list[1], self.numbers_list[2], self.numbers_list[3], self.numbers_list[4], self.numbers_list[5])
        self.lastTimeCheck = self.lastTimeRecorded

        self.csv_file = 'last_run_date.csv'

    def create_pygame_home(self, layout_lst):  # creates the completed pygame maze
        self.__maze_loop(layout_lst, self.__check_home_layout)  # loops through the maze, putting walls, floors in place
        self.__maze_loop(layout_lst, self.__check_home_elements)

    @staticmethod
    def __maze_loop(maze_lst: list, check_maze_cell):  # loops through every cell in the maze
        row_num = -1
        for row in maze_lst:
            row_num += 1
            col_num = -1

            for cell in row:
                col_num += 1
                position = (col_num * gf.tile_size, row_num * gf.tile_size)
                check_maze_cell(cell, position)

    def __check_home_layout(self, cell: str, position: tuple):
        if cell == "X":  # if there are walls
            mz_lay.WallHidden(position, [self.__game_camera, self.__wall_sprites])
            # all the groups that belong to the sprite class

        if cell == "Y":
            mz_lay.WallVisible(position, [self.__game_camera, self.__wall_sprites])

        if cell in " P":  # if there are floor tiles, including on the player
            self.floor = mz_lay.Floor(position, [self.__game_camera])

    def __check_home_elements(self, cell: str, position: tuple):
        if cell == "P":
            self.chip = pet.Pet(position, [self.__game_camera], self.__wall_sprites)


    def compareTimeHours (self):
    #
        currentTime = datetime.now()
        difference = currentTime - self.lastTimeCheck
        diffHours = (difference.total_seconds() / 10)#hange this to 3600 later

        if (diffHours > 1):
        #
            print("hange should happen")
            self.lastTimeCheck = currentTime
            return int(diffHours)
        #
        return 0
    #
    def compareTimeDays(self):
    #
        currentTime = datetime.now()

    def updatePet (self, chip):
    #
        diffHours = self.compareTimeHours()
        if (diffHours > 0):
        #
            chip.updatePet(diffHours)
        #
    #
    def run_level(self):
        self.__game_camera.draw_camera_offset()
        self.__game_camera.update()
        self.updatePet(self.chip)
        self.debug_time()

    def debug_time(self):
        current_time = datetime.now()

        # Extract hours, minutes, and seconds
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second