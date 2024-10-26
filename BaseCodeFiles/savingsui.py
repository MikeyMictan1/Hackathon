import sys
import pygame

import gamechange as g_change
import globalfunctions as gf
import buttons as btn
from ingamemenus import *
import SavingsAcc as sav_acc

class SavingsMenu(InGameMenu):
    """
    Description:
        Class for the controls menu UI that can be opened at any time while the player is in a level.

    Inherits:
        InGameMenu: inherits from the in game menu for certain attributes such as menu_overlay, escape_counter and
        in_game_menu_state

    Attributes:
        __control_set_image (pygame.Surface): Image containing all the controls of the game
    """
    def __init__(self):
        super().__init__()
        ...


    def display_menu(self):
        """
        Description:
            Displays the controls menu on the screen.
        """
        # makes sure the menu will open and close after open/close buttons are pressed
        if self.escape_counter % 2 == 0:
            self.in_game_menu_state = False

        self.screen.blit(self.menu_overlay, (gf.img_centre(self.menu_overlay)[0], gf.img_centre(self.menu_overlay)[1]))

