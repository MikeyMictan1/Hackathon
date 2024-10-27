import sys
import time

import pygame

import gamechange as g_change
import globalfunctions as gf
import buttons as btn
from ingamemenus import *
from investment import StockMarket
from datetime import datetime, timedelta
from player import Player


class StocksMenu(InGameMenu):
    """
    Description:
        Class for the controls menu UI that can be opened at any time while the player is in a level.

    Inherits:
        InGameMenu: inherits from the in game menu for certain attributes such as menu_overlay, escape_counter and
        in_game_menu_state

    Attributes:
        __control_set_image (pygame.Surface): Image containing all the controls of the game
    """
    def __init__(self,player, chip):
        super().__init__(player, chip)
        self.player = player
        self.chip = chip
        self.stockMarket = StockMarket()

                                            # return         grey overlay
        self.__in_game_menu_graphics_dict = {"continue": [], "overlay": [], "Buy": [], "Sell": []}
        self.__in_game_menu_graphics_dict = gf.import_graphics_dict("ingamemenu", self.__in_game_menu_graphics_dict,
                                                                 "../Graphics")

        self.__quit_txt_pos = (gf.screen_width // 1.3, gf.screen_height // 1.3)
        self.__quit_option = btn.OptionPress(self.quit_txt_white, self.quit_txt_yellow, self.__quit_txt_pos)


        self.__continue_txt_white = self.__in_game_menu_graphics_dict["continue"][0]
        self.__continue_txt_yellow = self.__in_game_menu_graphics_dict["continue"][1]
        self.__continue_txt_pos = (gf.screen_width // 1.3, gf.screen_height // 1.75)
        self.__continue_option = btn.OptionPress(self.__continue_txt_white, self.__continue_txt_yellow,
                                             self.__continue_txt_pos)

        self.menu_overlay = self.__in_game_menu_graphics_dict["overlay"][0]
        self.menu_overlay = pygame.transform.scale(self.menu_overlay, (1500, 800))

        self.extract_txt_white = self.__in_game_menu_graphics_dict["extract"][0]
        self.extract_txt_yellow = self.__in_game_menu_graphics_dict["extract"][1]

        self.deposit_txt_white = self.__in_game_menu_graphics_dict["deposit"][0]
        self.deposit_txt_yellow = self.__in_game_menu_graphics_dict["deposit"][1]


        # deposit button
        self.add_savings_pos = (gf.img_centre(self.deposit_txt_white)[0], gf.screen_height // 3)
        self.add_savings_option = btn.OptionPress(self.deposit_txt_white, self.deposit_txt_yellow, self.add_savings_pos)

        # extract button
        self.extract_savings_pos = (gf.img_centre(self.extract_txt_white)[0], gf.screen_height // 2)
        self.extract_savings_option = btn.OptionPress(self.extract_txt_white, self.extract_txt_yellow, self.extract_savings_pos)

        self.__in_game_menu_txt = gf.medium_title_font.render("Savings' Account Menu", 1, gf.white)
        self.balance_txt = gf.medium_title_font.render("Balance", 1, gf.white)

        self.savings_txt = gf.medium_title_font.render("Savings", 1, gf.white)
        # --- GRAPHICS ---

        self.escape_counter = 0



    def run_menu(self):
        """
        Description:
            sets up the menu - sets its state to "true", and plays the menu open sound
        """
        self.escape_counter += 1
        self.in_game_menu_state = True

    def display_menu(self):
        """
        Description:
            Displays the controls menu on the screen.
        """
        # makes sure the menu will open and close after open/close buttons are pressed

        if self.escape_counter % 2 == 0:  # makes sure esc will open AND close the in game menu
            self.in_game_menu_state = False
        self.balance_num = gf.medium_title_font.render(f"{self.player.currentBalance:.2f}cc", 1, gf.white)
        self.savings_num = gf.medium_title_font.render(f"{self.player.savings_balance:.2f}cc", 1, gf.white)

        self.screen.blit(self.menu_overlay, (gf.img_centre(self.menu_overlay)[0], gf.img_centre(self.menu_overlay)[1]))
        self.screen.blit(self.__in_game_menu_txt, (gf.img_centre(self.__in_game_menu_txt)[0]-150, gf.screen_height // 30))

        self.screen.blit(self.balance_txt, (gf.screen_width// 1.4, gf.screen_height // 30))
        self.screen.blit(self.balance_num, (gf.screen_width // 1.4, gf.screen_height // 10))

        self.screen.blit(self.savings_txt, (gf.screen_width// 1.4, gf.screen_height // 3))
        self.screen.blit(self.savings_num, (gf.screen_width // 1.4, gf.screen_height // 2.5))

        # draws menu buttons
        self.__continue_option.draw(pygame.display.get_surface())
        self.__quit_option.draw(pygame.display.get_surface())

        self.add_savings_option.draw(pygame.display.get_surface())
        self.extract_savings_option.draw(pygame.display.get_surface())

        # deposit money
        if self.add_savings_option.pressed:
            self.player.savings_balance += 10
            self.player.currentBalance -= 10
            time.sleep(0.2)
            self.add_savings_option.pressed = False

        # extract money
        if self.extract_savings_option.pressed and self.player.savings_balance > 0:
            self.player.savings_balance -= 10
            self.player.currentBalance += 10
            time.sleep(0.2)
            self.extract_savings_option.pressed = False

        # continue button
        if self.__continue_option.pressed:  # if continue button pressed, close menu
            self.escape_counter += 1
            self.in_game_menu_state = False
            self.__continue_option.pressed = False

        if self.__quit_option.pressed:  # quits the game if "quit" is pressed
            pygame.quit()
            sys.exit()



