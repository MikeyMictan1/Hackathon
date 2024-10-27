import pygame
import globalfunctions as gf
import mainmenu as mn_menu
import homelevel as home_lvl
from BaseCodeFiles import levellayout as lvl
import gamechange as g_change
import shopui as ig_menu
import savingsui as sav_menu
from BaseCodeFiles.globalfunctions import tile_size
import savings as sav
import stockmarketui as stk_menu
import resetui as res_menu

#hi
class Main:
    def __init__(self):
        pygame.init()
        # initial setups
        self.__screen = pygame.display.set_mode((gf.screen_width, gf.screen_height))
        pygame.display.set_caption("Hackathon Title")
        self.__clock = pygame.time.Clock()
        self.__in_game = True
        self.__main_menu = mn_menu.MainMenu()
        self.__in_game = True

        # level initialisation
        self.__home_level = home_lvl.HomeLevel(lvl.home)
        self.game_over = g_change.GameOver()
        self.in_game_menu = ig_menu.ShopMenu(self.__home_level.player, self.__home_level.chip)
        self.savings_menu = sav_menu.SavingsMenu(self.__home_level.player, self.__home_level.chip)
        self.stk_menu = stk_menu.StockMenu(self.__home_level.player, self.__home_level.chip)
        self.res_menu = res_menu.ResetMenu(self.__home_level.player, self.__home_level.chip)
        self.savings = sav.Savings(self.__home_level.player)

        # decor stuffs
        self.decorations_img = pygame.image.load("../Graphics/ingamemenu/decor_pic.PNG")
        self.decorations_img = pygame.transform.scale(self.decorations_img, (150, 150))

    def run(self):
        while self.__in_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.__in_game = False
                    break

                # in-game menu
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_TAB):
                    self.in_game_menu.run_menu()

                if event.type == pygame.KEYDOWN and (event.key == pygame.K_c):
                    self.savings_menu.run_menu()

                if event.type == pygame.KEYDOWN and (event.key == pygame.K_s):
                    self.stk_menu.run_menu()

                if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE):
                    self.res_menu.run_menu()

            self.__screen.fill("black")

            # --- PLAYS THE GAME ---
            self.play_game()

            # --- CHECKS IF IN MAIN MENU ---
            if self.__main_menu.in_menu:
                self.__main_menu.menu()

            # -- CHECKS IF IN SHOP MENU ---
            if self.in_game_menu.in_game_menu_state:  # if we open the in game menu by pressing ESC
                self.__handle_in_game_menu()

            # -- CHECKS IF IN SAVINGS MENU --
            if self.savings_menu.in_game_menu_state:
                self.__handle_savings_menu()

            # -- CHECKS IF IN STOCK MENU ---
            if self.stk_menu.in_game_menu_state:
                self.__handle_stocks_menu()

            # -- CHECKS IF IN RESET MENU --
            if self.res_menu.in_game_menu_state:
                self.__handle_reset_menu()

            self.saving_time()
            self.check_decor()
            pygame.display.update()
            self.__clock.tick(gf.FPS)

    def __handle_stocks_menu(self):
        self.stk_menu.display_menu()

    def __handle_reset_menu(self):
        self.res_menu.display_menu()

    def __handle_savings_menu(self):
        """
        Description:
            Displays the controls menu on the screen.
        """
        self.savings_menu.display_menu()

    def __handle_in_game_menu(self):
        if self.in_game_menu.display_menu():
            # recreates all levels and returns us to the menu
            ...

        if self.savings_menu.in_game_menu_state:
            self.savings_menu.in_game_menu_state = False
            self.savings_menu.escape_counter += 1

    def play_game(self):
        if self.__main_menu.play_pressed:
            self.__main_menu.in_menu = False
            self.__home_level.run_level()
            self.check_game_over(self.__home_level)
            self.__main_menu.game_on = False


    def check_game_over(self, home_lvl):
        if home_lvl.chip.happiness <= 0 or home_lvl.chip.hunger <= 0 or home_lvl.chip.thirst <= 0 or home_lvl.player.currentBalance <= 0:
            if home_lvl.chip.happiness <= 0:
                home_lvl.chip.happiness += 10

            if home_lvl.chip.hunger <= 0:
                home_lvl.chip.hunger += 10

            if home_lvl.chip.thirst <= 0:
                home_lvl.chip.thirst += 10

            if home_lvl.player.currentBalance <= 0:
                home_lvl.player.currentBalance += 10

            home_lvl.chip.resetStats()
            self.game_over.run()

    def check_decor(self):
        if self.in_game_menu.decor_bought:
            self.__screen.blit(self.decorations_img, (tile_size*7, tile_size))

        if self.in_game_menu.decor_bought and self.res_menu.decor_flag:
            self.in_game_menu.decor_bought = False
            self.res_menu.decor_flag = True

    def saving_time(self):
        self.savings.run()

main = Main()
main.run()