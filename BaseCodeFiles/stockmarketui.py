from ingamemenus import *

class StockMenu(InGameMenu):
    def __init__(self,player, chip):
        super().__init__(player, chip)
        self.player = player
        self.chip = chip

        self.__in_game_menu_graphics_dict = {"continue": [], "overlay": [], "buy": []}
        self.__in_game_menu_graphics_dict = gf.import_graphics_dict("ingamemenu", self.__in_game_menu_graphics_dict,
                                                                    "../Graphics")

        self.__quit_txt_pos = (gf.screen_width // 1.3, gf.screen_height // 1.3)
        self.__quit_option = btn.OptionPress(self.quit_txt_white, self.quit_txt_yellow, self.__quit_txt_pos)

        # INHERITED ---
        self.__continue_txt_white = self.__in_game_menu_graphics_dict["continue"][0]
        self.__continue_txt_yellow = self.__in_game_menu_graphics_dict["continue"][1]
        self.__continue_txt_pos = (gf.screen_width // 1.3, gf.screen_height // 1.75)
        self.__continue_option = btn.OptionPress(self.__continue_txt_white, self.__continue_txt_yellow,
                                             self.__continue_txt_pos)

        self.menu_overlay = self.__in_game_menu_graphics_dict["overlay"][0]
        self.menu_overlay = pygame.transform.scale(self.menu_overlay, (1500, 800))
        # INHERITED ---

        self.__in_game_menu_txt = gf.medium_title_font.render("The Stock Market", 1, gf.white)
        self.balance_txt = gf.medium_title_font.render("Balance", 1, gf.white)
        self.escape_counter = 0

        # STOCKS
        self.buy_stock1_pos = (gf.img_centre(self.buy_txt_white)[0], gf.screen_height // 3)
        self.buy_stock1_option = btn.OptionPress(self.buy_txt_white, self.buy_txt_yellow, self.buy_stock1_pos)

        self.buy_stock2_pos = (gf.img_centre(self.buy_txt_white)[0], gf.screen_height // 2)
        self.buy_stock2_option = btn.OptionPress(self.buy_txt_white, self.buy_txt_yellow, self.buy_stock2_pos)

        self.buy_stock3_pos = (gf.img_centre(self.buy_txt_white)[0], gf.screen_height // 1.5)
        self.buy_stock3_option = btn.OptionPress(self.buy_txt_white, self.buy_txt_yellow, self.buy_stock3_pos)

        self.buy_stock4_pos = (gf.img_centre(self.buy_txt_white)[0], gf.screen_height // 1.2)
        self.buy_stock4_option = btn.OptionPress(self.buy_txt_white, self.buy_txt_yellow, self.buy_stock4_pos)



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

        self.screen.blit(self.menu_overlay, (gf.img_centre(self.menu_overlay)[0], gf.img_centre(self.menu_overlay)[1]))
        self.screen.blit(self.__in_game_menu_txt, (gf.img_centre(self.__in_game_menu_txt)[0]-150, gf.screen_height // 30))

        self.screen.blit(self.balance_txt, (gf.screen_width// 1.4, gf.screen_height // 30))
        self.screen.blit(self.balance_num, (gf.screen_width // 1.4, gf.screen_height // 10))

        # draws menu buttons
        self.__continue_option.draw(pygame.display.get_surface())
        self.__quit_option.draw(pygame.display.get_surface())
        self.buy_stock1_option.draw(pygame.display.get_surface())
        self.buy_stock2_option.draw(pygame.display.get_surface())
        self.buy_stock3_option.draw(pygame.display.get_surface())
        self.buy_stock4_option.draw(pygame.display.get_surface())

        # continue button
        if self.__continue_option.pressed:  # if continue button pressed, close menu
            self.escape_counter += 1
            self.in_game_menu_state = False
            self.__continue_option.pressed = False

        if self.__quit_option.pressed:  # quits the game if "quit" is pressed
            pygame.quit()
            sys.exit()


