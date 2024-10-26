import pygame
import globalfunctions as gf
import mainmenu as mn_menu
import homelevel as home_lvl
from BaseCodeFiles import levellayout as lvl
import gamechange as g_change

#hi
class Main:
    def __init__(self):
        pygame.init()
        # initial setup
        self.__screen = pygame.display.set_mode((gf.screen_width, gf.screen_height))
        pygame.display.set_caption("Hackathon Title")
        self.__clock = pygame.time.Clock()
        self.__in_game = True
        self.__main_menu = mn_menu.MainMenu()
        self.__in_game = True

        # level initialisation
        self.__home_level = home_lvl.MazeLevel(lvl.home)
        self.game_over = g_change.GameOver()

    def run(self):
        while self.__in_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.__in_game = False
                    break

                # in-game menu
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_TAB or event.key == pygame.K_ESCAPE):
                    pass

                if event.type == pygame.KEYDOWN and (event.key == pygame.K_c):
                    pass

            self.__screen.fill("black")

            # --- PLAYS THE GAME ---
            self.play_game()

            # --- CHECKS IF IN MAIN MENU ---
            if self.__main_menu.in_menu:
                self.__main_menu.menu()


            pygame.display.update()
            self.__clock.tick(gf.FPS)

    def play_game(self):
        if self.__main_menu.play_pressed:
            self.__main_menu.in_menu = False
            self.__home_level.run_level()
            self.__main_menu.game_on = False

    def check_game_over(self):
        self.game_over.run(...)

main = Main()
main.run()