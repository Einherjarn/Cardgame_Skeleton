import pygame
from card_hand import card_hand

# Initialization stuff
pygame.init()
size = (640,480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("cardgame skeleton")

all_sprites_list = pygame.sprite.Group()

Continue = True
clock = pygame.time.Clock()

card1 = card_hand()
card1.rect.x = 320
card1.rect.y = 240
all_sprites_list.add(card1)

card2 = card_hand()
card2.rect.x = 370
card2.rect.y = 240
all_sprites_list.add(card2)

# Main Program Logic Loop
while Continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False
    
    all_sprites_list.update()
    screen.fill((155,155,155))
    all_sprites_list.draw(screen)
    # updating screen
    pygame.display.flip()

    # 60 fps glorious pc gaming masterrace
    clock.tick(60)
# out of mainloop, close dis
pygame.quit()
