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

font_cardname = pygame.freetype.Font(None, 14)
font_health = pygame.freetype.Font(None, 16)
font_description = pygame.freetype.Font(None, 18)
font_stamcost = pygame.freetype.Font(None, 36)
font_stamina = pygame.freetype.Font(None, 42)
font_cardselection = pygame.freetype.Font(None, 42)
font_playername = pygame.freetype.Font(None, 42)

pygame.display.set_caption("cardgame skeleton")
sprites_group = pygame.sprite.Group()
Continue = True
clock = pygame.time.Clock()

player1 = Player("dev_testing_deck_longsword", "player 1")
player2 = Player("dev_testing_deck_longsword", "player 2")
initiative = None
opener = None

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
    # render cards, in 2 rows if more than 5
    for i in range(len(player.hand)):
        if (player.hand[i] and i < 5):
            player.hand[i].cardsprite.rect.x = 50+(i*150)
            player.hand[i].cardsprite.rect.y = 250+(i*10)
            player.hand[i].artsprite.rect.x = 50+(i*150)+3
            player.hand[i].artsprite.rect.y = 250+(i*10)+3
        elif (player.hand[i]):
            player.hand[i].cardsprite.rect.x = 50+((i-5)*150)
            player.hand[i].cardsprite.rect.y = 450+((i-5)*10)
            player.hand[i].artsprite.rect.x = 50+((i-5)*150)+3
            player.hand[i].artsprite.rect.y = 450+((i-5)*10)+3

    # add all card sprites to spritegroup
    screen.fill((200,200,200))
    for i in range(len(player.hand)):
        render_card(player.hand[i])
        
    # individual screen elements
    font_stamina.render_to(screen, (120,10), str(player.stamina), (0, 255, 0))
    font_playername.render_to(screen, (120,50), str(player.name), (0, 0, 0))
    cardonmouse = card_on_mouse(player) 
    if (cardonmouse):
        font_cardselection.render_to(screen, (120,100), cardonmouse.name, (0, 0, 0))
        render_card(cardonmouse)
    # health indicators
    playersprite = Sprite("player_status_image.png")
    playersprite.rect.x = 5
    playersprite.rect.y = 5
    sprites_group.add(playersprite)
    sprites_group.update()
    sprites_group.draw(screen)
    sprites_group.empty()
    #head
    font_health.render_to(screen, (55,15), str(player.health[0]), (255, 0, 0))
    #r-arm
    font_health.render_to(screen, (10,50), str(player.health[1]), (255, 0, 0))
    #r-torso
    font_health.render_to(screen, (40,50), str(player.health[2]), (255, 0, 0))
    #r-leg
    font_health.render_to(screen, (40,160), str(player.health[3]), (255, 0, 0))
    #l-arm
    font_health.render_to(screen, (100,50), str(player.health[4]), (255, 0, 0))
    #l-torso
    font_health.render_to(screen, (70,50), str(player.health[5]), (255, 0, 0))
    #l-leg
    font_health.render_to(screen, (70,160), str(player.health[6]), (255, 0, 0))
    
    # updating screen
    pygame.display.flip()   

# todo, black graphics transition screen, wait for any input to acknowledge seatswitch
def hotseat(player):
    if(player == player1):
        player = player2
    else:
        player = player1
    return player

def resolve(opener, opponent, attack, counter):
    # head, r-arm, r-torso, r-leg, l-arm, l-torso, l-leg
    result_opener = [0,0,0,0,0,0,0]
    result_opponent = [0,0,0,0,0,0,0]

    for i in range(len(attack.power)):
        result_opponent[i] = (counter.defend[i] - attack.power[i])
    for i in range(len(counter.power)):
        result_opener[i] = (attack.defend[i] - counter.power[i])
        
    for i in range(len(result_opponent)):
        opponent.health[i] += result_opponent[i]
    for i in range(len(result_opener)):
        opener.health[i] += result_opener[i]

# Main Program Logic Loop
while Continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False
        else:     
        # all primary game logic goes under here
            # start of exchange, current player undefined, so we do startup stuff.
            try:
                player
            except NameError:
                player = player1
                initiative = player1
                player1.draw(5)
                player1.setStance()
                player2.draw(5)
                player2.setStance()
            # turn begins
            # draw if hand not full
            if (len(player.hand) < 10):
                player.draw(1)
            # ask current player for card
            card = play_card(player)
            if (card):
                if(opener == None):
                    opener = player
                player.stack.append(card)
                if((initiative != player and card.take_initiative == True) or (initiative == player and card.take_initiative == True and opener != player)):
                    # took initiative from opponent, now we evaluate the exchange
                    initiative = player
                    print(initiative.name)
                    if opener == player1:
                        opponent = player2
                    else:
                        opponent = player1
                    # evaluate each attack of the opener against defense used by opponent
                    print("resolving exchange..")
                    for i in range(len(opponent.stack)):
                        resolve(opener, opponent, opener.stack[i], opponent.stack[i])
                    # reset exchange stuff
                    opener.stack = []
                    opponent.stack = []
                    opener = None
                    opponent = None
                player = hotseat(player)
                if(opener == None):
                    player = initiative
                
    render_player(player)
    # 60 fps glorious pc gaming masterrace
    clock.tick(60)
# out of mainloop, close dis
pygame.quit()
