import pygame

class GameCamera(pygame.sprite.Group):
    """
    Description:
        Class for the camera that makes sure the character stays in the centre of the screen, with everything else moving
        around the character.

    Inherits:
        pygame.sprite.Group: Inherits from pygame's sprite class to make sprite interactions and functions easier to
        handle.

    Attributes:
        __screen (pygame.Surface):  the screen for which the camera will draw objects onto in their correct positions.
        __character_movement_offset (tuple): Vector for the offset to move all sprites due to the character moving.
        __character_image_offset (tuple): vector for the offset to move the character due to the size of the characters
        images, so that the image of the character is in the same place as its rect.
    """
    def __init__(self):
        """
        Description:
            Initialisation function for the GameCamera class. Initialises the screen and character offsets.
        """
        # general setup
        super().__init__()  # super init to get methods and attributes from the sprite class
        self.__screen = pygame.display.get_surface()
        self.__character_movement_offset = pygame.math.Vector2()
        self.__character_image_offset = (-75, -50)

    def draw_camera_offset(self):
        """
        Description:
            Draws all sprites onto the screen, draws them with an offset, which is the character's current position
            subtract half the screen width/height, so the character is always drawn in the centre of the screen.

        Parameters:
            character (chara.Character): The character sprite currently playing the game
        """

        for sprite in self.sprites():
            # adding a vector to a sprite to effect where the sprite will be drawn on the screen, draw the sprites image
            # in the same place as the rectangle.
            character_movement_offset_pos = sprite.rect.topleft
            self.__screen.blit(sprite.image, character_movement_offset_pos)


