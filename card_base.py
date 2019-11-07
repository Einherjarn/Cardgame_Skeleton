import pygame
from sprite import Sprite

class Card_base():
    def __init__(self):
        super().__init__()
        self.name = "cardname"
        self.cardsprite = Sprite("card_base.png")
        self.artsprite = Sprite("card_art_base.png")
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
