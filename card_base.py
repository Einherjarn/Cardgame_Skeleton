import pygame

class Card_base(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.image = pygame.image.load("card_base.png")
        self.image_art = pygame.image.load("card_art_base.png")
        self.typeimage = ""
        #self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.basecost = 0
        self.range = 0
        # head, r-arm, r-torso, r-leg, l-arm, l-torso, l-leg
        self.target = [False,False,False,False,False,False,False]
        self.defend = [False,False,False,False,False,False,False]
        self.power = [0,0,0,0,0,0,0]
        self.defense_power = [0,0,0,0,0,0,0]
        self.take_initiative = True
        self.description = "description"
        self.modifiers = []
