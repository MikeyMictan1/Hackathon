import time

from shopui import *
import investment as invest

class StockMenu(ShopMenu):
    def __init__(self,player, chip):
        super().__init__(player, chip)
        self.player = player
        self.chip = chip
        self.stock_market = invest.StockMarket()

        self.__in_game_menu_graphics_dict = {"continue": [], "overlay": [], "buy": [], "sell": []}
        self.__in_game_menu_graphics_dict = gf.import_graphics_dict("ingamemenu", self.__in_game_menu_graphics_dict,
                                                                    "../Graphics")

        self.__quit_txt_pos = (gf.screen_width // 1.3, gf.screen_height // 1.3)
        self.__quit_option = btn.OptionPress(self.quit_txt_white, self.quit_txt_yellow, self.__quit_txt_pos)

        # sell
        self.sell_txt_white = self.__in_game_menu_graphics_dict["sell"][0]
        self.sell_txt_yellow = self.__in_game_menu_graphics_dict["sell"][1]

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
        self.buy_stock1_pos = (gf.img_centre(self.buy_txt_white)[0]+300, 300)
        self.buy_stock1_option = btn.OptionPress(self.buy_txt_white, self.buy_txt_yellow, self.buy_stock1_pos)
        self.buy_stock1_option.transform(90,50)

        self.sell_stock1_pos = (gf.img_centre(self.sell_txt_white)[0]+400, 300)
        self.sell_stock1_option = btn.OptionPress(self.sell_txt_white, self.sell_txt_yellow, self.sell_stock1_pos)
        self.sell_stock1_option.transform(90,50)

        # stock 2
        self.buy_stock2_pos = (gf.img_centre(self.buy_txt_white)[0]+300, 350)
        self.buy_stock2_option = btn.OptionPress(self.buy_txt_white, self.buy_txt_yellow, self.buy_stock2_pos)
        self.buy_stock2_option.transform(90,50)

        self.sell_stock2_pos = (gf.img_centre(self.sell_txt_white)[0]+400, 350)
        self.sell_stock2_option = btn.OptionPress(self.sell_txt_white, self.sell_txt_yellow, self.sell_stock2_pos)
        self.sell_stock2_option.transform(90,50)

        # stock 3
        self.buy_stock3_pos = (gf.img_centre(self.buy_txt_white)[0]+300, 400)
        self.buy_stock3_option = btn.OptionPress(self.buy_txt_white, self.buy_txt_yellow, self.buy_stock3_pos)
        self.buy_stock3_option.transform(90,50)

        self.sell_stock3_pos = (gf.img_centre(self.sell_txt_white)[0]+400, 400)
        self.sell_stock3_option = btn.OptionPress(self.sell_txt_white, self.sell_txt_yellow, self.sell_stock3_pos)
        self.sell_stock3_option.transform(90,50)

        # stock 4
        self.buy_stock4_pos = (gf.img_centre(self.buy_txt_white)[0]+300, 450)
        self.buy_stock4_option = btn.OptionPress(self.buy_txt_white, self.buy_txt_yellow, self.buy_stock4_pos)
        self.buy_stock4_option.transform(90,50)

        self.sell_stock4_pos = (gf.img_centre(self.buy_txt_white)[0]+400, 450)
        self.sell_stock4_option = btn.OptionPress(self.sell_txt_white, self.sell_txt_yellow, self.sell_stock4_pos)
        self.sell_stock4_option.transform(90,50)



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
        self.stock_table_img = pygame.image.load("stockMarket.png")
        self.stock_table_img = pygame.transform.scale(self.stock_table_img, (800, 400))

        if self.escape_counter % 2 == 0:  # makes sure esc will open AND close the in game menu
            self.in_game_menu_state = False

        self.balance_num = gf.medium_title_font.render(f"{self.player.currentBalance:.2f}cc", 1, gf.white)

        self.screen.blit(self.menu_overlay, (gf.img_centre(self.menu_overlay)[0], gf.img_centre(self.menu_overlay)[1]))
        self.screen.blit(self.__in_game_menu_txt, (gf.img_centre(self.__in_game_menu_txt)[0]-150, gf.screen_height // 30))

        self.screen.blit(self.balance_txt, (gf.screen_width// 1.4, gf.screen_height // 30))
        self.screen.blit(self.balance_num, (gf.screen_width // 1.4, gf.screen_height // 10))

        self.screen.blit(self.stock_table_img, (0, gf.screen_height // 2 - self.stock_table_img.get_height() // 2))
        # draws menu buttons
        self.__continue_option.draw(pygame.display.get_surface())
        self.__quit_option.draw(pygame.display.get_surface())
        self.buy_stock1_option.draw(pygame.display.get_surface())
        self.buy_stock2_option.draw(pygame.display.get_surface())
        self.buy_stock3_option.draw(pygame.display.get_surface())
        self.buy_stock4_option.draw(pygame.display.get_surface())

        self.sell_stock1_option.draw(pygame.display.get_surface())
        self.sell_stock2_option.draw(pygame.display.get_surface())
        self.sell_stock3_option.draw(pygame.display.get_surface())
        self.sell_stock4_option.draw(pygame.display.get_surface())

        # continue button
        if self.__continue_option.pressed:  # if continue button pressed, close menu
            self.escape_counter += 1
            self.in_game_menu_state = False
            self.__continue_option.pressed = False

        # stock 1 -----
        if self.buy_stock1_option.pressed:
            stock1 = self.stock_market.readCSV()[0]
            stock1.buyStock(1, self.player, self.stock_market)
            time.sleep(0.2)
            self.buy_stock1_option.pressed = False

        if self.sell_stock1_option.pressed:
            stock1 = self.stock_market.readCSV()[0]
            if stock1.numberOwned > 0:
                stock1.sellStock(1, self.player, self.stock_market)
            time.sleep(0.2)
            self.sell_stock1_option.pressed = False

        # stock 2 -----
        if self.buy_stock2_option.pressed:
            stock2 = self.stock_market.readCSV()[1]
            stock2.buyStock(1, self.player, self.stock_market)
            time.sleep(0.2)
            self.buy_stock2_option.pressed = False

        if self.sell_stock2_option.pressed:
            stock2 = self.stock_market.readCSV()[1]
            if stock2.numberOwned > 0:
                stock2.sellStock(1, self.player, self.stock_market)
            time.sleep(0.2)
            self.sell_stock2_option.pressed = False

        # stock 3 -----
        if self.buy_stock3_option.pressed:
            stock3 = self.stock_market.readCSV()[2]
            stock3.buyStock(1, self.player, self.stock_market)
            time.sleep(0.2)
            self.buy_stock3_option.pressed = False

        if self.sell_stock3_option.pressed:
            stock3 = self.stock_market.readCSV()[2]
            if stock3.numberOwned > 0:
                stock3.sellStock(1, self.player, self.stock_market)
            time.sleep(0.2)
            self.sell_stock3_option.pressed = False

        # stock 4 -----
        if self.buy_stock4_option.pressed:
            stock4 = self.stock_market.readCSV()[3]
            stock4.buyStock(1, self.player, self.stock_market)
            time.sleep(0.2)
            self.buy_stock4_option.pressed = False

        if self.sell_stock4_option.pressed:
            stock4 = self.stock_market.readCSV()[3]
            if stock4.numberOwned > 0:
                stock4.sellStock(1, self.player, self.stock_market)
            time.sleep(0.2)
            self.sell_stock4_option.pressed = False

        if self.__quit_option.pressed:  # quits the game if "quit" is pressed
            pygame.quit()
            sys.exit()


