import pygame
import sys

import buttons as btn
import globalfunctions as gf


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

        # menu text
        self.menu_txt_white = self.game_change_graphics_dict["menu"][0]
        self.menu_txt_yellow = self.game_change_graphics_dict["menu"][1]
        self.__menu_txt_pos = (gf.screen_width // 10, gf.screen_height // 1.5)
        self.__menu_option = btn.OptionPress(self.menu_txt_white, self.menu_txt_yellow, self.__menu_txt_pos)

        # quit game text
        self.quit_txt_white = self.game_change_graphics_dict["quit"][0]
        self.quit_txt_yellow = self.game_change_graphics_dict["quit"][1]
        self.__quit_txt_pos = (gf.screen_width // 1.4, gf.screen_height // 1.5)
        self.__quit_option = btn.OptionPress(self.quit_txt_white, self.quit_txt_yellow, self.__quit_txt_pos)

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
        self.__menu_option.draw(pygame.display.get_surface())
        self.__quit_option.draw(pygame.display.get_surface())

        if self.__menu_option.pressed:  # returns player to the menu if "menu" pressed
            self.game_win_state = False
            self.game_over_state = False

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
        self.__game_over_graphics_dict = {"background": [], "fallen_player": []}
        self.__game_over_graphics_dict = gf.import_graphics_dict("gameover", self.__game_over_graphics_dict,
                                                                 "../Graphics")
        self.__background = self.__game_over_graphics_dict["background"][0]
        self.__background = pygame.transform.scale(self.__background, (gf.screen_width, gf.screen_height))

        # other text
        self.__game_over_txt = self.game_change_font.render("GAME OVER!", 1, gf.white)
        self.__game_over_music = pygame.mixer.Sound("../Audio/game_over_music.mp3")

    def run(self, points: float):
        """
        Description:
            Runs the game over menu, checking for button presses and displaying the number of points the player
            achieved.

        Parameters:
            points (float): The number of points the character is on once the game over menu is reached.
        """
        self.__end_points = int(points)
        self.__score_txt = self.game_change_points_font.render(f"POINTS BEFORE DEATH:{self.__end_points}", 1, gf.white)

        #  plays game over music
        pygame.mixer.stop()
        self.__game_over_music.play()
        self.__game_over_music.set_volume(0.1)

        while self.game_over_state:  # while we are in the game over menu
            self.event_quit()

            # game over visuals
            self.screen.blit(self.__background, (0, 0))
            self.screen.blit(self.__game_over_txt, (gf.img_centre(self.__game_over_txt)[0], gf.screen_height // 20))
            self.screen.blit(self.__score_txt, (gf.img_centre(self.__score_txt)[0], gf.screen_height // 4))

            # animations for the character icon in the middle of the game over screen
            self.frame += self.frame_speed
            if self.frame >= len(self.__game_over_graphics_dict["fallen_player"]):
                self.frame = 0

            character_image = self.__game_over_graphics_dict["fallen_player"][int(self.frame)]
            character_image = pygame.transform.scale(character_image, (200, 160))
            self.screen.blit(character_image, (gf.img_centre(character_image)[0], gf.img_centre(character_image)[1]))

            # draw buttons onto menu
            self.display_menu()


class GameWin(GameChange):
    """
    Description:
        Class that handles the game win UI menu when the character beats the game.

    Inherits:
        GameChange: Inherits from game change, to get key features such as the quit and menu buttons.

    Attributes:
        game_win_state (bool): Flag that checks if the game win menu should be active
        __game_win_graphics_dict (dict): Dictionary of all images used for the game win menu
        __background (pygame.Surface): Background image for the game over menu
        __logo_image (pygame.Surface): image of the logo of the game
        __game_win_txt (pygame.font.render): Text that says "VICTORY" to be drawn on the screen
        __amazd_txt (pygame.font.render): Extra text that appears on the game win screen
        __game_win_music (pygame.mixer.Sound): Game win music to be played during the game win menu
    """
    def __init__(self):
        """
        Description:
            initialisation function for the GameWin class.
        """
        super().__init__()
        self.game_win_state = True

        # Graphics
        self.__game_win_graphics_dict = {"background": [], "victory_slime": []}
        self.__game_win_graphics_dict = gf.import_graphics_dict("gamewin", self.__game_win_graphics_dict, "../Graphics")

        self.__background = self.__game_win_graphics_dict["background"][0]
        self.__background = pygame.transform.scale(self.__background, (gf.screen_width, gf.screen_height))
        self.__logo_image = pygame.transform.scale(pygame.image.load(f"../Graphics/amazd_logo.png"), (140, 280))

        # other text
        self.__game_win_txt = self.game_change_font.render("VICTORY!", 1, gf.white)
        self.__amazd_txt = self.game_change_points_font.render("(You Have Amaz'd Me)", 1, gf.white)
        self.__game_win_music = pygame.mixer.Sound("../Audio/victory_music.mp3")

    def run(self, points: float):
        """
        Description:
            Runs the game win menu, checking for button presses and displaying the number of points the player
            achieved.

        Parameters:
            points (float): The number of points the character is on once the game win menu is reached.
        """
        self.__end_points = int(points)
        self.__score_txt = self.game_change_points_font.render(f"POINTS:{self.__end_points}", 1, gf.white)

        #  plays game win music
        pygame.mixer.stop()
        self.__game_win_music.play()
        self.__game_win_music.set_volume(0.1)

        while self.game_win_state:  # while in the game win menu
            self.event_quit()

            # game over visuals
            self.screen.blit(self.__background, (0, 0))
            self.screen.blit(self.__game_win_txt, (gf.img_centre(self.__game_win_txt)[0], gf.screen_height // 20))
            self.screen.blit(self.__amazd_txt, (gf.img_centre(self.__amazd_txt)[0], gf.screen_height // 6))
            self.screen.blit(self.__score_txt, (gf.img_centre(self.__score_txt)[0], gf.screen_height // 3))
            self.screen.blit(self.__logo_image, (gf.img_centre(self.__logo_image)[0], gf.screen_height // 1.5))

            #  animations for the slime enemy icon in the middle of the game over screen
            self.frame += self.frame_speed
            if self.frame >= len(self.__game_win_graphics_dict["victory_slime"]):
                self.frame = 0

            character_image = self.__game_win_graphics_dict["victory_slime"][int(self.frame)]
            character_image = pygame.transform.scale(character_image, (200, 160))
            self.screen.blit(character_image, (gf.img_centre(character_image)[0], gf.img_centre(character_image)[1]))

            # draw buttons onto menu
            self.display_menu()
