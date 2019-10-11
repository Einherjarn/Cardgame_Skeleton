import pygame
import pygame.freetype
from card_base import card_base

# Initialization stuff
pygame.init()
size = (640,480)
screen = pygame.display.set_mode(size)
font_description = pygame.freetype.Font(None, 18)
font_stamcost = pygame.freetype.Font(None, 36)
pygame.display.set_caption("cardgame skeleton")
sprites_group = pygame.sprite.Group()
Continue = True
clock = pygame.time.Clock()
cardlist = []

# placeholder example cards
card1 = card_base()
card1.rect.x = 50
card1.rect.y = 150
card1.basecost = 10
card1.description = "test custom description"
cardlist.append(card1)

card2 = card_base()
card2.rect.x = 350
card2.rect.y = 150
cardlist.append(card2)

# Main Program Logic Loop
while Continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False

    # add all card sprites to spritegroup
    for i in range(len(cardlist)):
        sprites_group.add(cardlist[i])
    
    sprites_group.update()
    screen.fill((200,200,200))
    
    sprites_group.draw(screen)

    for i in range(len(cardlist)):
        font_description.render_to(screen, (cardlist[i].rect.x+20, cardlist[i].rect.y+165), cardlist[i].description, (0, 0, 0))
        font_stamcost.render_to(screen, (cardlist[i].rect.x+10, cardlist[i].rect.y+10), str(cardlist[i].basecost), (0, 255, 0))
    # updating screen
    pygame.display.flip()

    # 60 fps glorious pc gaming masterrace
    clock.tick(60)
# out of mainloop, close dis
pygame.quit()
