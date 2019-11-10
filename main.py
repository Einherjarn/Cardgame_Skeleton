import pygame
import pygame.freetype
from sprite import Sprite
from card_base import Card_base
from player import Player

# Initialization stuff
pygame.init()
size = (960,720)
screen = pygame.display.set_mode(size)
font_description = pygame.freetype.Font(None, 18)
font_stamcost = pygame.freetype.Font(None, 36)
font_cardname = pygame.freetype.Font(None, 15)
pygame.display.set_caption("cardgame skeleton")
sprites_group = pygame.sprite.Group()
Continue = True
clock = pygame.time.Clock()

player1 = Player("dev_testing_deck_longsword")
player2 = Player("dev_testing_deck_longsword")
stack = []

def resolve(card):
    pass
    #stub

def play_card(player):
    pass

# Main Program Logic Loop
while Continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False
        else:     
        # all primary game logic goes under here, before the rendering stuff
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
    # rendering stuff
    for i in range(len(player.hand)):
        if player.hand[i]:
            player.hand[i].cardsprite.rect.x = 100+(i*150)
            player.hand[i].cardsprite.rect.y = 350+(i*10)
            player.hand[i].artsprite.rect.x = 100+(i*150)+3
            player.hand[i].artsprite.rect.y = 350+(i*10)+3

    # add all card sprites to spritegroup
    screen.fill((200,200,200))
    for i in range(5):
        sprites_group.add(player.hand[i].cardsprite)
        sprites_group.add(player.hand[i].artsprite)
        sprites_group.update()
        sprites_group.draw(screen)
        font_description.render_to(screen, (player.hand[i].cardsprite.rect.x+20, player.hand[i].cardsprite.rect.y+210), player.hand[i].description, (0, 0, 0))
        font_stamcost.render_to(screen, (player.hand[i].cardsprite.rect.x+10, player.hand[i].cardsprite.rect.y+10), str(player.hand[i].basecost), (0, 255, 0))
        font_cardname.render_to(screen, (player.hand[i].cardsprite.rect.x+5, player.hand[i].cardsprite.rect.y+180), player.hand[i].name, (0, 0, 0))
        sprites_group.empty()

    #for i in range(len(player1.hand)):

    # updating screen
    pygame.display.flip()

    # 60 fps glorious pc gaming masterrace
    clock.tick(60)
# out of mainloop, close dis
pygame.quit()
