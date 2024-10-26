import pygame

import homelayout as mz_lay
import globalfunctions as gf
import camera as cam
#import pet as chip
from datetime import datetime
import csv, os

class MazeLevel:
    """
    Description:
        Class that takes the depth-first created maze as a list, and "translates" it into pygame, in order to be played.

        Acts as the interface for which enemies and characters interact.

    Attributes:
        __powerup_sprites (pygame.sprite.Group): Sprite group consisting of speed powerup sprites
        __coin_sprites (pygame.sprite.Group): Sprite group consisting of coin sprites
        __health_pot_sprites (pygame.sprite.Group): Sprite group consisting of health potion sprites
        __exit_sprites (pygame.sprite.Group): Sprite group consisting of exit portal sprites
        __enemy_sprites (pygame.sprite.Group): Sprite group consisting of enemy sprites
        __sword_sprites (pygame.sprite.Group): Sprite group consisting of sword sprites
        __game_camera (pygame.sprite.Group): Sprite group consisting of the camera that the character centres around
        __wall_sprites (pygame.sprite.Group): Sprite group consisting of maze wall sprites

        is_active (bool): Flag that checks if the current maze level is active
        level_type (str): What type of level the current level is (e.g. tutorial, normal, boss)
    """
    def __init__(self, layout_list: list):
        """
        Description:
            Initialisation method for the MazeLevel class

        parameters:
            maze_list (list): The depth-first generated maze, as a list.
        """
        # sprite groups setup
        self.__powerup_sprites = pygame.sprite.Group()
        self.__coin_sprites = pygame.sprite.Group()
        self.__health_pot_sprites = pygame.sprite.Group()
        self.__exit_sprites = pygame.sprite.Group()
        self.__enemy_sprites = pygame.sprite.Group()
        self.__sword_sprites = pygame.sprite.Group()
        self.__wall_sprites = pygame.sprite.Group()
        self.__game_camera = cam.GameCamera()

        # maze creation
        self.create_pygame_home(layout_list)

        # other setup
        self.is_active = True
        self.level_type = "normal"

        self.csv_file = 'last_run_date.csv'

    def create_pygame_home(self, layout_lst):  # creates the completed pygame maze
        """
        Description:
            Creates the completed maze in pygame with sprites.

        Parameters:
            layout_lst (list): The depth-first maze as a list.
        """
        self.__maze_loop(layout_lst, self.__check_home_layout)  # loops through the maze, putting walls, floors in place


    @staticmethod
    def __maze_loop(maze_lst: list, check_maze_cell):  # loops through every cell in the maze
        """
        Description:
        Loops through every cell of the maze, translating the cells strings into pygame sprites.

        Parameters:
            maze_lst (list): The depth-first maze as a list.
            check_maze_cell: Checks the contents of the cell. Will create a sprite at that cell position depending on
            what the cell was.
        """
        row_num = -1
        for row in maze_lst:
            row_num += 1
            col_num = -1

            for cell in row:
                col_num += 1
                position = (col_num * gf.tile_size, row_num * gf.tile_size)
                check_maze_cell(cell, position)

    def __check_home_layout(self, cell: str, position: tuple):
        """
        Description:
        Checks a cell, and makes that cell into a wall or floor sprite, depending on what letter the cell is.

        Parameters:
            cell (list): One individual letter in the maze, that represents a sprite such as a wall, floor, etc.
            position (tuple): Position of where the sprite should be drawn onto the screen.
        """
        if cell == "X":  # if there are walls
            mz_lay.WallHidden(position, [self.__game_camera, self.__wall_sprites])
            # all the groups that belong to the sprite class

        if cell == "Y":
            mz_lay.WallVisible(position, [self.__game_camera, self.__wall_sprites])

        if cell in " P":  # if there are floor tiles, including on the player
            self.floor = mz_lay.Floor(position, [self.__game_camera])

    def __check_home_elements(self, cell: str, position: tuple):
        if cell == "P":
            #self.chip = pet.Pet(position, [self.__game_camera], self.__wall_sprites)
            ...

    def compareTime (self):
    #
        currentTime = datetime.now()
        difference = currentTime - self.lastTimeCheck
        diffHours = (difference.total_seconds() / 3600)
        print(diffHours)
        if diffHours > 1:
        #
            self.lastTimeCheck = currentTime
            return int(diffHours)
        #
        return 0
    #
    def updatePet (self):
    #
        diffHours = self.compareTime()
        if (diffHours > 0):
        #
            a = 0
        #
    #
    def run_level(self):
        self.__game_camera.draw_camera_offset()
        self.__game_camera.update()
        self.update_time()

    # Functions that deal with time every day
    def update_time(self):
        last_run_date = self.check_last_date()
        current_date = datetime.now()
        if last_run_date is None or current_date.date() > last_run_date.date():

            print("hi")
            # Update the CSV with the current date
            self.check_current_date()

    def check_current_date(self):
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            current_date = datetime.now().strftime('%Y-%m-%d')
            writer.writerow([current_date])

    def check_last_date(self):
        if os.path.exists(self.csv_file):
            with open(self.csv_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    # Parse the stored date into a datetime object
                    last_run_date = datetime.strptime(row[0], '%Y-%m-%d')
                    return last_run_date
        return None