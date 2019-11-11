from card_base import Card_base
from player import Player
from random import seed
from random import randint

def drawSelf(player, n):
    if(player==player1):
        target = player1
    else:
        target = player2
    for i in range(n):
        target.hand.append(target.deck.pop())

def drawOpp(player, n):
    if(player==player1):
        target = player2
    else:
        target = player1
    for i in range(n):
        target.hand.append(target.deck.pop())

def discardSelf(player, n):
    if(player==player1):
        target = player1
    else:
        target = player2
    target.discard.append(target.hand.pop(n))

def discardOpp(player, n):
    if(player==player1):
        target = player2
    else:
        target = player1
    target.discard.append(target.hand.pop(n))

def discardRandomSelf(player, n):
    if(player==player1):
        target = player1
    else:
        target = player2
    maxval = len(target.hand)-1
    for i in range(n):
        discardSelf(player, random.randint(0, maxval))

def discardRandomOpp(player, n):
    if(player==player1):
        target = player1
    else:
        target = player2
    maxval = len(target.hand)-1
    for i in range(n):
        discardSelf(player, random.randint(0, maxval))

def bind(player):
    pass
