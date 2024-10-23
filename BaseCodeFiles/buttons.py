import pygame


class OptionPress:
    """
    Description:
        Class that handles all buttons that can be pressed in the game.

    Attributes:
        __option_image (pygame.Surface): The button image that will be drawn onto the screen
        __position (tuple): The screen co-ordinates of where the button will be drawn
        __image1 (pygame.Surface): The first possible image the button could be (button with white text)
        __image2 (pygame.Surface): The second possible image the button could be (button with yellow text)
        __button_rect (pygame.Rect): Rectangular area of where the button object is on the screen
        pressed (bool): flag variable for if the button has been pressed
    """
    def __init__(self, image1: pygame.Surface, image2: pygame.Surface, position: tuple):
        """
        Description:
            Initialisation function for the OptionPress class. Initialises the buttons possible images, and where
            the button is drawn on the screen.

        Parameters:
            image1 (pygame.Surface): The first possible image the button could be (button with white text)
            image2 (pygame.Surface): The second possible image the button could be (button with yellow text)
            position (tuple): The screen co-ordinates of where the button will be drawn
        """
        # initialising
        self.__option_image = image1
        self.__position = position
        self.__image1 = image1
        self.__image2 = image2

        self.__button_rect = self.__option_image.get_rect(topleft=self.__position)
        self.pressed = False

    def __mouse_press(self):
        """
        Description:
            Checks if a mouse presses the button, if so, the buttons pressed variable is set to true.
        """
        __mouse_rect = pygame.mouse.get_pos()
        # if hovering mouse over option, button1 sound and change image to yellow text image
        if self.__button_rect.collidepoint(__mouse_rect):
            self.__option_image = self.__image2
            # if button clicked, set pressed to true
            if pygame.mouse.get_pressed()[0] == 1 and not self.pressed:
                self.pressed = True

        else:
            self.__option_image = self.__image1

    def draw(self, screen: pygame.Surface):
        """
        Description:
            Draws the button onto the screen in its specified position, and constantly checks for mouse presses

        Parameters:
            screen (pygame.Surface): the screen for which the button will be drawn onto
           """
        self.__mouse_press()
        screen.blit(self.__option_image, self.__position)
