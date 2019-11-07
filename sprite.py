import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, file):
        super().__init__()
        self.image = pygame.image.load(file)
        #self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
