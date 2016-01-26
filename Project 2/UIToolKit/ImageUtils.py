import pygame

class ImageUtils:
    #Bah ugly as shit
    Screen = pygame.display.set_mode((600,600))

    def scale(image, rectangle):
        return pygame.transform.smoothscale(image, rectangle.size)

     
    def loadImage(image):
        return pygame.image.load("Content/" + image).convert_alpha()