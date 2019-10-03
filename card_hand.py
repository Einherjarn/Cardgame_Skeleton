import pygame

class card_hand(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_dev_example.png")
        #self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
