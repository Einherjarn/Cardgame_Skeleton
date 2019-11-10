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

# placeholder example cards
"""
card1 = Card_base()
card1.rect.x = 50
card1.rect.y = 150
card1.basecost = 10
card1.description = "test custom description"
cardlist.append(card1)

card2 = Card_base()
card2.rect.x = 350
card2.rect.y = 150
cardlist.append(card2)
"""

player1turn = True
player1 = Player("dev_testing_deck_longsword")
player2 = Player("dev_testing_deck_longsword")

# Main Program Logic Loop
while Continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False
    # all primary game logic goes under here, before the rendering stuff
    if player1turn:
        player = player1
    else:
        player = player2
    # placeholder draw 5 cards if hand empty
    player.draw(5)
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
