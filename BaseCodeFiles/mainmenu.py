import sys
import pygame
import buttons as btn
import globalfunctions as gf


class MainMenu:
    """
    Description:
        Class that creates the main menu UI.
    """

    def __init__(self):
        """
        Description:
            Initialisation function for the main menu class.
        """
        self.__quit_option = None
        self.__play_button = None
        self.in_menu = True  # in the menu?
        self.play_pressed = False  # button1 option pressed?

        # loading logo graphics
        self.__screen = pygame.display.set_mode((gf.screen_width, gf.screen_height))

        self.__menu_graphics_dict = {"background": [], "button1": [], "quit": []}
        self.__menu_graphics_dict = gf.import_graphics_dict("menu", self.__menu_graphics_dict, "../Graphics")

        # menu titles and background
        self.__main_menu_title = gf.title_font.render("Pet Payday", 1, gf.white)
        self.__background = self.__menu_graphics_dict["background"][0]
        self.__background = pygame.transform.scale(self.__background, (gf.screen_width, gf.screen_height))

        # menu buttons graphics
        self.__first_button_white = self.__menu_graphics_dict["button1"][0]
        self.__first_button_yellow = self.__menu_graphics_dict["button1"][1]
        self.__first_button_pos = (gf.screen_width // 1.5, gf.screen_height // 1.5)

        self.__quit_button_white = self.__menu_graphics_dict["quit"][0]
        self.__quit_button_yellow = self.__menu_graphics_dict["quit"][1]
        self.__quit_button_pos = (gf.screen_width // 10, gf.screen_height // 1.5)

    def play_button_pressed(self):
        """
        Description:
            whatever we want to happen when the first button gets pressed
        """
        self.in_menu = False

    def menu(self):
        """
        Description:
            Main method that runs the main menu.
        """
        while self.in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # menu visuals
            self.__screen.blit(self.__background, (0, 0))
            self.__screen.blit(self.__main_menu_title,
                               (gf.img_centre(self.__main_menu_title)[0], gf.screen_height // 5))


            # drawing buttons onto the screen
            self.handle_menu_buttons()

            pygame.display.update()

    def handle_menu_buttons(self):
        """
        Description:
            Draws menu buttons on the screen, and checks if they have been pressed.
        """
        # button1 menu option
        self.__play_button = btn.OptionPress(self.__first_button_white, self.__first_button_yellow, self.__first_button_pos)
        self.__play_button.draw(pygame.display.get_surface())

        # first button option
        if self.__play_button.pressed:  # plays the game if "button1" pressed
            self.play_button_pressed()
            self.play_pressed = True

        # quit button option
        self.__quit_option = btn.OptionPress(self.__quit_button_white, self.__quit_button_yellow, self.__quit_button_pos)
        self.__quit_option.draw(pygame.display.get_surface())

        if self.__quit_option.pressed:
            pygame.quit()
            sys.exit()

