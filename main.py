import math
import pygame
import pygame.freetype
from sprite import Sprite
from card_base import Card_base
from player import Player

# Initialization stuff
pygame.init()
size = (960,720)
screen = pygame.display.set_mode(size)

font_cardname = pygame.freetype.Font(None, 15)
font_description = pygame.freetype.Font(None, 18)
font_stamcost = pygame.freetype.Font(None, 36)
font_stamina = pygame.freetype.Font(None, 42)
font_cardselection = pygame.freetype.Font(None, 42)

pygame.display.set_caption("cardgame skeleton")
sprites_group = pygame.sprite.Group()
Continue = True
clock = pygame.time.Clock()

player1 = Player("dev_testing_deck_longsword", "player 1")
player2 = Player("dev_testing_deck_longsword", "player 2")
stack = []

def resolve(card):
    pass
    #stub

def card_on_mouse(player):
    lowdist = 9999
    for i in range(len(player.hand)):
        if player.hand[i]:
            (x,y) = pygame.mouse.get_pos()
            dist = math.sqrt( ((x-(player.hand[i].cardsprite.rect.x+130))**2)+((y-player.hand[i].cardsprite.rect.y)**2) )
            if(dist < lowdist):
                lowdist = dist
                card = player.hand[i]
    return card

def play_card(player):
    render_player(player)
    (b1,b2,b3) = pygame.mouse.get_pressed()
    if(b1 > 0):
        print(card_on_mouse(player).name)
        return card_on_mouse(player)
        
# rendering stuff
def render_card(card):
    sprites_group.add(card.cardsprite)
    sprites_group.add(card.artsprite)
    sprites_group.update()
    sprites_group.draw(screen)
    font_description.render_to(screen, (card.cardsprite.rect.x+20, card.cardsprite.rect.y+210), card.description, (0, 0, 0))
    font_stamcost.render_to(screen, (card.cardsprite.rect.x+10, card.cardsprite.rect.y+10), str(card.basecost), (0, 255, 0))
    font_cardname.render_to(screen, (card.cardsprite.rect.x+5, card.cardsprite.rect.y+180), card.name, (0, 0, 0))
    sprites_group.empty()

def render_player(player):
    for i in range(len(player.hand)):
        if player.hand[i]:
            player.hand[i].cardsprite.rect.x = 100+(i*150)
            player.hand[i].cardsprite.rect.y = 350+(i*10)
            player.hand[i].artsprite.rect.x = 100+(i*150)+3
            player.hand[i].artsprite.rect.y = 350+(i*10)+3

    # add all card sprites to spritegroup
    screen.fill((200,200,200))
    for i in range(len(player.hand)):
        render_card(player.hand[i])
        
    # individual screen elements
    font_stamina.render_to(screen, (10,10), str(player.stamina), (0, 255, 0))
    cardonmouse = card_on_mouse(player) 
    if (cardonmouse):
        font_cardselection.render_to(screen, (80,10), cardonmouse.name, (0, 0, 0))
        render_card(cardonmouse)

    # updating screen
    pygame.display.flip()   

# Main Program Logic Loop
while Continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False
        else:     
        # all primary game logic goes under here
            #start of exchange, current player undefined, so we do startup stuff.
            try:
                player
            except NameError:
                player = player1
                player1.draw(5)
                player1.setStance()
                player2.draw(5)
                player2.setStance()
            #turn begins
            #draw if hand not full
            if (len(player.hand) < 9):
                player.draw(1)
            #ask current player for card to play, and resolve it
            resolve(play_card(player))
    render_player(player)
    # 60 fps glorious pc gaming masterrace
    clock.tick(60)
# out of mainloop, close dis
pygame.quit()
