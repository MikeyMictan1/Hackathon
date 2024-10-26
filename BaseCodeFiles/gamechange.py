import pygame
import sys

import buttons as btn
import globalfunctions as gf
from BaseCodeFiles.globalfunctions import img_centre, screen_height


class GameChange:
    """
    Description:
        The parent class that handles "game change" menus such as the game over and game win menus.

    Attributes:
        screen (pygame.Surface): Screen that the menus will be drawn onto
        clock (pygame.time.Clock): Clock object that controls the frame rate of the game
        game_over_state (bool): Flag that checks if game over has been reached
        game_win_state (bool): Flag that checks if game win has been reached
        __end_points (float): The number of points the player reached once a game change menu is reached
        __score_txt (pygame.font.Render): The text that says "score" to be drawn on the screen

        game_change_graphics_dict (dict): Dictionary containing graphics for the game change menus
        menu_txt_white (pygame.Surface): Image for the menu button in white
        menu_txt_yellow (pygame.Surface): Image for the menu button in yellow
        __menu_txt_pos (tuple): Position on the screen to draw the menu button
        __menu_option (btn.OptionPress): Making the menu position and image into a clickable button

        quit_txt_white (pygame.Surface): Image for the quit button in white
        quit_txt_yellow (pygame.Surface): Image for the quit button in yellow
        __quit_txt_pos (tuple): Position on the screen to draw the quit button
        __quit_option (btn.OptionPress): Making the quit position and image into a clickable button

        game_change_font (pygame.font.Font): Font used to write text onto game change menus
        game_change_points_font (pygame.font.Font): Font used to write the points text onto game change menus

        frame (float): Current frame used for animation
        frame_speed (float): Speed of animations for animated parts of the game change menu
    """
    def __init__(self):
        """
        Description:
            Initialisation function for the game change class.
        """
        # initial setup
        pygame.init()
        self.screen = pygame.display.set_mode((gf.screen_width, gf.screen_height))
        self.clock = pygame.time.Clock()
        self.game_over_state = None
        self.game_win_state = None
        self.__end_points = None
        self.__score_txt = None

        # game change graphics
        self.game_change_graphics_dict = {"menu": [], "quit": []}
        self.game_change_graphics_dict = gf.import_graphics_dict("gamechange", self.game_change_graphics_dict,
                                                                 "../Graphics")

        # quit game text
        self.quit_txt_white = self.game_change_graphics_dict["quit"][0]
        self.quit_txt_yellow = self.game_change_graphics_dict["quit"][1]
        self.__quit_txt_pos = img_centre(self.quit_txt_yellow)
        self.__quit_option = btn.OptionPress(self.quit_txt_white, self.quit_txt_yellow, (self.__quit_txt_pos[0], screen_height//1.2))

        self.game_change_font = pygame.font.Font("../Fonts/Pixel.ttf", 100)
        self.game_change_points_font = pygame.font.Font("../Fonts/Pixel.ttf", 60)

        self.frame = 0
        self.frame_speed = 0.1

    @staticmethod
    def event_quit():
        """
        Description:
            Runs the event game loop, so the game closes if someone quits the game.

            Static method.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def display_menu(self):
        """
        Description:
            Draws the menu buttons in the game, and handles if they are pressed.

            Pygame and the screen are updated.
        """
        # draw buttons
        self.__quit_option.draw(pygame.display.get_surface())
        if self.__quit_option.pressed:  # quits the game if "quit" is pressed
            pygame.quit()
            sys.exit()

        pygame.display.update()
        self.clock.tick(gf.FPS)


class GameOver(GameChange):
    """
    Description:
        Class that handles the game over UI menu when the character dies.

    Inherits:
        GameChange: Inherits from game change, to get key features such as the quit and menu buttons.

    Attributes:
        game_over_state (bool): Flag that checks if the game over menu should be active
        __game_over_graphics_dict (dict): Dictionary of all images used for the game over menu
        __background (pygame.Surface): Background image for the game over menu
        __game_over_txt (pygame.font.render): Text that says "GAME OVER" to be drawn on the screen
        __game_over_music (pygame.mixer.Sound): Game over music to be played during the game over menu
    """
    def __init__(self):
        """
        Description:
            initialisation function for the GameOver class.
        """
        super().__init__()
        self.game_over_state = True

        # Graphics importing
        self.__game_over_graphics_dict = {"background": []}
        self.__game_over_graphics_dict = gf.import_graphics_dict("gameover", self.__game_over_graphics_dict,
                                                                 "../Graphics")
        self.__background = self.__game_over_graphics_dict["background"][0]
        self.__background = pygame.transform.scale(self.__background, (gf.screen_width, gf.screen_height))

        # other text
        self.__game_over_txt = gf.title_font.render("Chip Died! xD", 1, gf.white)

#
    def run(self):
        while self.game_over_state:  # while we are in the game over menu
            self.event_quit()

            # game over visuals
            self.screen.blit(self.__background, (0, 0))
            self.screen.blit(self.__game_over_txt, (gf.img_centre(self.__game_over_txt)[0], gf.screen_height // 20))

            # draw buttons onto menu
            self.display_menu()


