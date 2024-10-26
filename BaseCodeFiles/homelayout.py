import pygame
import random
import os


class WallVisible(pygame.sprite.Sprite):
    """
    Description:
        Class for maze visible wall sprites. "Visible" meaning that the tile below them is not another wall, so the
        side of the wall is visible. ("Y" walls when generated in DepthFirstMaze)

    Inherits:
        pygame.sprite.Group: Inherits from pygame sprite class to make sprite interactions and functions easier.

    Attributes:
        image (pygame.Surface): Image of the visible wall tile
        rect (pygame.Rect): Rectangular area of the visible wall sprite in a certain location.
    """
    def __init__(self, pos: tuple, groups: list):
        """
        Description:
            Initialisation function for the visible wall sprite class.

        Attributes:
            pos (tuple): Position of the visible wall tile on the screen.
            groups (list): the sprite groups that the visible wall class belongs to
        """
        super().__init__(groups)
        self.image = pygame.image.load(
            f"../Graphics/wall/crackedbrick.png").convert_alpha()  # making a visible wall surface
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect(topleft=pos)


class WallHidden(pygame.sprite.Sprite):
    """
    Description:
        Class for maze hidden wall sprites. "Hidden" meaning that the tile below them is another wall, so the side of
        the wall is not visible. ("X" walls when generated in DepthFirstMaze)

    Inherits:
        pygame.sprite.Group: Inherits from pygame sprite class to make sprite interactions and functions easier.

    Attributes:
        image (pygame.Surface): Image of the hidden wall tile
        rect (pygame.Rect): Rectangular area of the hidden wall sprite in a certain location.
    """
    def __init__(self, pos: tuple, groups: list):
        """
        Description:
            Initialisation function for the wall hidden sprite class.

        Attributes:
            pos (tuple): Position of the hidden wall tile on the screen.
            groups (list): the sprite groups that the hidden wall class belongs to
        """
        super().__init__(groups)
        self.image = pygame.image.load(
            f"../Graphics/wall/crackedbrickhidden.png").convert_alpha()  # making a hidden wall surface
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect(topleft=pos)


class Floor(pygame.sprite.Sprite):
    """
    Description:
        Class for maze floor sprites. Floor sprites should have sprites such as character, enemy, powerup, health potion
        all be overlaid on top of the floor.

    Inherits:
        pygame.sprite.Group: Inherits from pygame sprite class to make sprite interactions and functions easier.

    Attributes:
        image (pygame.Surface): Image of the floor tile
        rect (pygame.Rect): Rectangular area of the floor sprite in a certain location.
    """
    def __init__(self, pos: tuple, groups: list):
        """
        Description:
            Initialisation function for the floor sprite class.

        Attributes:
            pos (tuple): Position of the floor tile on the screen.
            groups (list): the sprite groups that the floor class belongs to
        """
        super().__init__(groups)
        self.images = os.listdir("../Graphics/floor")
        self.image = pygame.image.load(
            f"../Graphics/floor/{random.choice(self.images)}").convert_alpha()  # making a floor surface
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect(topleft=pos)
