import pygame
import os

# --- GAME SETTINGS SETUP ---
# game size
tile_size = 150
screen_width = 8* tile_size
screen_height = 5 * tile_size

# game frames per second, and number of levels
FPS = 60
pygame.init()

# fonts and colours
font = pygame.font.Font("../Fonts/Pixel.ttf", 100)
title_font = pygame.font.Font("../Fonts/sheepish.ttf", 100)
medium_title_font = pygame.font.Font("../Fonts/sheepish.ttf", 50)
smaller_title_font = pygame.font.Font("../Fonts/sheepish.ttf", 20)
general_font = pygame.font.Font("../Fonts/Primer.otf", 100)
white = (255, 255, 255)
# --- GAME SETTINGS SETUP ---


def img_centre(image: pygame.Surface):
    """
    Description:
        Gives the position of where an image should be, in order for the image to appear in the centre of the screen

    Parameters:
        image (pygame.Surface): The image to be placed in the centre of the screen

    Returns:
        [width, height]: tuple of the width and height of an image in the centre of the screen
    """
    width = screen_width // 2 - image.get_width() // 2
    height = screen_height // 2 - image.get_height() // 2
    return [width, height]


def load_graphics(filepath: str):
    """
    Description:
        Loads all the images in a folder, and adds it to a list

    Parameters:
        filepath (str): The file location of the folder containing all the images

    Returns:
        graphic_surface_list (list): The list containing all the images
    """
    graphic_surface_list = []

    for image in os.listdir(filepath):  # for every image in a file location
        image_filepath = f"{filepath}/{image}"  # get images fill filepath

        loaded_image = pygame.image.load(image_filepath)  # load image
        graphic_surface_list.append(loaded_image)  # append loaded image to a list

    return graphic_surface_list  # returns the list of all loaded images


def import_graphics_dict(sprite_name: str, animation_dict: dict, filepath: str):
    """
    Description:
        Imports all the pygame images from load_graphics and places them into a dictionary.

    Parameters:
        sprite_name (str): The name of the sprite, for which images are being loaded
        animation_dict (dict): The dictionary that will be filled with image surfaces
        filepath (str): The file location of the folder containing all the images

    Returns:
        animation_dict (dict): The final dictionary containing all the loaded pygame image surfaces
    """
    main_path = f"{filepath}/{sprite_name}/"

    for animation_type in animation_dict.keys():  # for each key in the dictionary
        # add the respective image files to that key in the dictionary
        animation_dict[animation_type] = load_graphics(main_path + animation_type)

    return animation_dict
