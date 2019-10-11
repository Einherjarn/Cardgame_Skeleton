import pygame

class card_base(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_base.png")
        #self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.basecost = 0
        self.description = "description"
