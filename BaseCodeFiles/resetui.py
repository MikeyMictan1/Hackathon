import time

from shopui import *
import investment as invest

class ResetMenu(ShopMenu):
    def __init__(self,player, chip):
        super().__init__(player, chip)
        self.player = player
        self.chip = chip
        self.stock_market = invest.StockMarket()

        self.__in_game_menu_graphics_dict = {"continue": [], "overlay": [], "reset": []}
        self.__in_game_menu_graphics_dict = gf.import_graphics_dict("ingamemenu", self.__in_game_menu_graphics_dict,
                                                                    "../Graphics")

        self.__quit_txt_pos = (gf.img_centre(self.quit_txt_white)[0], gf.screen_height // 1.3)
        self.__quit_option = btn.OptionPress(self.quit_txt_white, self.quit_txt_yellow, self.__quit_txt_pos)

        self.reset_txt_white = self.__in_game_menu_graphics_dict["reset"][0]
        self.reset_txt_yellow = self.__in_game_menu_graphics_dict["reset"][1]
        self.reset_txt_pos = (gf.img_centre(self.reset_txt_white)[0], gf.img_centre(self.reset_txt_white)[1]-50)
        self.reset_option = btn.OptionPress(self.reset_txt_white, self.reset_txt_yellow, self.reset_txt_pos)

        # INHERITED ---
        self.__continue_txt_white = self.__in_game_menu_graphics_dict["continue"][0]
        self.__continue_txt_yellow = self.__in_game_menu_graphics_dict["continue"][1]
        self.__continue_txt_pos = (gf.img_centre(self.__continue_txt_white)[0], gf.screen_height // 1.75)
        self.__continue_option = btn.OptionPress(self.__continue_txt_white, self.__continue_txt_yellow,
                                             self.__continue_txt_pos)

        self.menu_overlay = self.__in_game_menu_graphics_dict["overlay"][0]
        self.menu_overlay = pygame.transform.scale(self.menu_overlay, (1500, 800))
        # INHERITED ---

        self.__in_game_menu_txt = gf.medium_title_font.render("Reset the game?", 1, gf.white)
        self.balance_txt = gf.medium_title_font.render("Balance", 1, gf.white)
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

        self.screen.blit(self.menu_overlay, (gf.img_centre(self.menu_overlay)[0], gf.img_centre(self.menu_overlay)[1]))
        self.screen.blit(self.__in_game_menu_txt, (gf.img_centre(self.__in_game_menu_txt)[0]-150, gf.screen_height // 30))


        # draws menu buttons
        self.__continue_option.draw(pygame.display.get_surface())
        self.__quit_option.draw(pygame.display.get_surface())
        self.reset_option.draw(pygame.display.get_surface())

        # continue button
        if self.__continue_option.pressed:  # if continue button pressed, close menu
            self.escape_counter += 1
            self.in_game_menu_state = False
            self.__continue_option.pressed = False

        if self.reset_option.pressed:
            #self.chip.resetStats()
            # brute-force method
            self.chip.hunger = 100
            self.chip.thirst = 100
            self.chip.happiness = 100
            self.player.currentBalance = 100
            self.player.savings_balance = 100

            self.reset_option.pressed = False
            time.sleep(0.2)

        if self.__quit_option.pressed:  # quits the game if "quit" is pressed
            pygame.quit()
            sys.exit()
