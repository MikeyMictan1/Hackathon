import sys
import pygame

import gamechange as g_change
import globalfunctions as gf
import buttons as btn
import time

class InGameMenu(g_change.GameChange):
    """
    Description:
        Class for the in-game menu UI that the player can open at any point in a level to quit, or return to the main
        menu

    Inherits:
        g_change.GameChange: Inherits from GameChange to use the menu and quit buttons in GameChange.

    Attributes:
        in_game_menu_state (bool): Flag that checks if the player is in the in-game menu
        __in_game_menu_graphics_dict (dict): Dictionary containing graphics used for the in-game menu
        __menu_txt_pos (tuple): new position of the menu button for the in-game menu
        __menu_option (btn.OptionPress): Menu button
        __quit_txt_pos (tuple): new position of the quit button for the in-game menu
        __quit_option (btn.OptionPress): Quit button

        __continue_txt_white (pygame.Surface): Image for the continue button in white
        __continue_txt_yellow (pygame.Surface): Image for the continue button in yellow
        __continue_txt_pos (tuple): Position on the screen to draw the continue button
        __continue_option (btn.OptionPress): Continue button

        menu_overlay (pygame.Surface): Overlay image that is drawn on the screen in the in-game menu
        __in_game_menu_txt (pygame.font.render): text to be displayed on the in-game menu
        __in_game_menu_sound (pygame.mixer.Sound): Sound to be played whenever the in-game menu is opened/closed
        escape_counter (int): The number of times a button that opens the in game menu has been pressed
    """
    def __init__(self, player, chip):
        """
        Description:
            Initialisation function for the in game menu class.
        """
        super().__init__()
        self.in_game_menu_state = False
        self.player = player
        self.chip = chip
        self.decor_bought = False

        # --- GRAPHICS ---
        self.__in_game_menu_graphics_dict = {"continue": [], "overlay": [], "buy": []}
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

        self.buy_txt_white = self.__in_game_menu_graphics_dict["buy"][0]
        self.buy_txt_yellow = self.__in_game_menu_graphics_dict["buy"][1]

        # buying buttons
        self.food_img = pygame.image.load("../Graphics/ingamemenu/food_pic.PNG")
        self.food_img = pygame.transform.scale(self.food_img, (80, 80))
        self.clothes_img = pygame.image.load("../Graphics/ingamemenu/clothes_pic.PNG")
        self.clothes_img = pygame.transform.scale(self.clothes_img, (80, 80))
        self.drinks_img = pygame.image.load("../Graphics/ingamemenu/water_pic.PNG")
        self.drinks_img = pygame.transform.scale(self.drinks_img, (80, 80))
        self.decorations_img = pygame.image.load("../Graphics/ingamemenu/decor_pic.PNG")
        self.decorations_img = pygame.transform.scale(self.decorations_img, (80, 80))


        self.buy_food_pos = (gf.img_centre(self.buy_txt_white)[0], gf.screen_height // 3)
        self.buy_food_option = btn.OptionPress(self.buy_txt_white, self.buy_txt_yellow, self.buy_food_pos)
        self.food_price_txt = gf.medium_title_font.render("Price: 5", 1, gf.white)

        self.buy_clothes_pos = (gf.img_centre(self.buy_txt_white)[0], gf.screen_height // 2)
        self.buy_clothes_option = btn.OptionPress(self.buy_txt_white, self.buy_txt_yellow, self.buy_clothes_pos)
        self.clothes_price_txt = gf.medium_title_font.render("Price: 5", 1, gf.white)

        self.buy_drinks_pos = (gf.img_centre(self.buy_txt_white)[0], gf.screen_height // 1.5)
        self.buy_drinks_option = btn.OptionPress(self.buy_txt_white, self.buy_txt_yellow, self.buy_drinks_pos)
        self.drinks_price_txt = gf.medium_title_font.render("Price: 5", 1, gf.white)

        self.buy_decorations_pos = (gf.img_centre(self.buy_txt_white)[0], gf.screen_height // 1.2)
        self.buy_decorations_option = btn.OptionPress(self.buy_txt_white, self.buy_txt_yellow, self.buy_decorations_pos)
        self.decorations_price_txt = gf.medium_title_font.render("Price: 5", 1, gf.white)

        self.__in_game_menu_txt = gf.title_font.render("SHOP", 1, gf.white)
        self.balance_txt = gf.medium_title_font.render(f"Balance:", 1, gf.white)
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
        Descriptions:
            Displays the in-game menu on the screen. checks for button presses.

        Returns:
            True: returns true if the menu button was pressed
        """
        if self.escape_counter % 2 == 0:  # makes sure esc will open AND close the in game menu
            self.in_game_menu_state = False
        self.balance_num = gf.medium_title_font.render(f"   {self.player.currentBalance:.2f}cc", 1, gf.white)

        self.screen.blit(self.menu_overlay, (gf.img_centre(self.menu_overlay)[0], gf.img_centre(self.menu_overlay)[1]))
        self.screen.blit(self.__in_game_menu_txt, (gf.img_centre(self.__in_game_menu_txt)[0], gf.screen_height // 30))
        self.screen.blit(self.balance_txt, (gf.screen_width// 1.4, gf.screen_height // 30))
        self.screen.blit(self.balance_num, (gf.screen_width // 1.4, gf.screen_height // 10))

        self.screen.blit(self.food_img, (gf.img_centre(self.buy_txt_white)[0]-380, gf.screen_height // 3 +20))
        self.screen.blit(self.clothes_img, (gf.img_centre(self.buy_txt_white)[0] - 380, gf.screen_height // 2 + 20))
        self.screen.blit(self.drinks_img, (gf.img_centre(self.buy_txt_white)[0] - 380, gf.screen_height // 1.5 + 20))
        self.screen.blit(self.decorations_img, (gf.img_centre(self.buy_txt_white)[0] - 380, gf.screen_height // 1.2 + 20))

        # draws menu buttons

        self.__continue_option.draw(pygame.display.get_surface())
        self.__quit_option.draw(pygame.display.get_surface())

        self.buy_food_option.draw(pygame.display.get_surface())
        self.screen.blit(self.food_price_txt, (gf.img_centre(self.buy_txt_white)[0]-250, gf.screen_height // 3 +30))

        self.buy_clothes_option.draw(pygame.display.get_surface())
        self.screen.blit(self.clothes_price_txt, (gf.img_centre(self.buy_txt_white)[0]-250, gf.screen_height // 2 +30))

        self.buy_drinks_option.draw(pygame.display.get_surface())
        self.screen.blit(self.drinks_price_txt, (gf.img_centre(self.buy_txt_white)[0]-250, gf.screen_height // 1.5 +30))

        self.buy_decorations_option.draw(pygame.display.get_surface())
        self.screen.blit(self.decorations_price_txt, (gf.img_centre(self.buy_txt_white)[0]-250, gf.screen_height // 1.2 +30))


        if self.buy_food_option.pressed:
            self.player.currentBalance -= 5
            self.chip.hunger += 5
            self.buy_food_option.pressed = False
            time.sleep(0.2)

        if self.buy_clothes_option.pressed:
            self.player.currentBalance -= 5
            self.buy_clothes_option.pressed = False
            time.sleep(0.2)

        if self.buy_drinks_option.pressed:
            self.player.currentBalance -= 5
            self.chip.thirst += 5
            self.buy_drinks_option.pressed = False
            time.sleep(0.2)

        if self.buy_decorations_option.pressed:
            self.decor_bought = True
            self.player.currentBalance -= 5
            self.chip.happiness += 5
            self.buy_decorations_option.pressed = False
            time.sleep(0.2)

        if self.__continue_option.pressed:  # if continue button pressed, close menu
            self.escape_counter += 1
            self.in_game_menu_state = False
            self.__continue_option.pressed = False

        if self.__quit_option.pressed:  # quits the game if "quit" is pressed
            pygame.quit()
            sys.exit()