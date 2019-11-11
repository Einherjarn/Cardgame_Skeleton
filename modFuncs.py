import math
import pygame
from card_base import Card_base
from player import Player
from random import seed
from random import randint

def card_on_mouse(player):
    lowdist = 9999
    for i in range(len(player.hand)):
        if player.hand[i]:
            (x,y) = pygame.mouse.get_pos()
            dist = math.sqrt( ((x-(player.hand[i].cardsprite.rect.x+130))**2)+((y-player.hand[i].cardsprite.rect.y-157)**2) )
            if(dist < lowdist):
                lowdist = dist
                card = player.hand[i]
    return card

# first argument player, 2nd last and last arguments player1, player2
def drawSelf(player, n, player1, player2):
    if(player==player1):
        target = player1
    else:
        target = player2
    target.draw(n)

def drawOpp(player, n, player1, player2):
    if(player==player1):
        target = player2
    else:
        target = player1
    target.draw(n)

def discardSelf(player, n, player1, player2):
    if(player==player1):
        target = player1
    else:
        target = player2
    target.discard.append(target.hand.pop(n))

def discardOpp(player, n, player1, player2):
    if(player==player1):
        target = player2
    else:
        target = player1
    target.discard.append(target.hand.pop(n))

def discardRandomSelf(player, n, player1, player2):
    if(player==player1):
        target = player1
    else:
        target = player2
    maxval = len(target.hand)-1
    for i in range(n):
        discardSelf(player, random.randint(0, maxval))

def discardRandomOpp(player, n, player1, player2):
    if(player==player1):
        target = player1
    else:
        target = player2
    maxval = len(target.hand)-1
    for i in range(n):
        discardSelf(player, random.randint(0, maxval))

def bind(player, player1, player2):
    player.invulnerable = promptTargetZone()

def feint(player, player1, player2):
    return promptTargetZone(player)

def promptTargetZone(player, player1, player2):
    pass
