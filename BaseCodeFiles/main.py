import pygame
import globalfunctions as gf
import mainmenu as mn_menu

class Main:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((gf.screen_width, gf.screen_height))
        pygame.display.set_caption("Hackathon Title")
        self.__clock = pygame.time.Clock()

        self.running = True
        self.__main_menu = mn_menu.MainMenu()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    break

                # in-game menu
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_TAB or event.key == pygame.K_ESCAPE):
                    pass

                if event.type == pygame.KEYDOWN and (event.key == pygame.K_c):
                    pass

            self.__screen.fill("black")

            # --- CHECKS IF IN MAIN MENU ---
            if self.__main_menu.in_menu:
                self.__main_menu.menu()


            pygame.display.update()
            self.__clock.tick(gf.FPS)

main = Main()
main.run()