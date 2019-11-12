import math
import sys
import pygame
import pygame.freetype
from modFuncs import *
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
player1.shuffle()
player2 = Player("dev_testing_deck_longsword", "player 2")
player2.shuffle()
initiative = None
opener = None

def run_arbitrary(name, args):
    """for i in range(len(args)):
        print(str(args[i]))"""
    possibles = globals().copy()
    possibles.update(locals())
    func = possibles.get(name)
    if not func:
         raise NotImplementedError("Function %s not implemented" % name)
    func(*args)

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
        card = card_on_mouse(player)
        # find and execute possible on-play modifiers
        for i in range(len(card.modifiers)):
            if(card.modifiers[i][1] == "OnPlay"):
                args = []
                for j in range(2,len(card.modifiers[i])):
                    args.append(card.modifiers[i][j])
                args.append(player1)
                args.append(player2)
                run_arbitrary(card.modifiers[i][0],args)
        print(card.name)
        player.discard(player.hand.index(card))
        return card

# add appropriate target icons to spritegroup
def render_targeticons(card):
    if(card.target[0]):
        sprite = Sprite("targeticon_head.png")
        sprite.rect.x = card.cardsprite.rect.x+240
        sprite.rect.y = card.cardsprite.rect.y+250
        sprites_group.add(sprite)
    if(card.target[1]):
        sprite = Sprite("targeticon_right_arm.png")
        sprite.rect.x = card.cardsprite.rect.x+232
        sprite.rect.y = card.cardsprite.rect.y+257
        sprites_group.add(sprite)
    if(card.target[2]):
        sprite = Sprite("targeticon_right_torso.png")
        sprite.rect.x = card.cardsprite.rect.x+238
        sprite.rect.y = card.cardsprite.rect.y+259
        sprites_group.add(sprite)
    if(card.target[3]):
        sprite = Sprite("targeticon_right_leg.png")
        sprite.rect.x = card.cardsprite.rect.x+232
        sprite.rect.y = card.cardsprite.rect.y+266
        sprites_group.add(sprite)
    if(card.target[4]):
        sprite = Sprite("targeticon_left_arm.png")
        sprite.rect.x = card.cardsprite.rect.x+249
        sprite.rect.y = card.cardsprite.rect.y+258
        sprites_group.add(sprite)
    if(card.target[5]):
        sprite = Sprite("targeticon_left_torso.png")
        sprite.rect.x = card.cardsprite.rect.x+245
        sprite.rect.y = card.cardsprite.rect.y+258
        sprites_group.add(sprite)
    if(card.target[6]):
        sprite = Sprite("targeticon_left_leg.png")
        sprite.rect.x = card.cardsprite.rect.x+248
        sprite.rect.y = card.cardsprite.rect.y+268
        sprites_group.add(sprite)

# add appropriate defense icons to spritegroup
def render_defenseicons(card):
    if(card.defend[0]):
        sprite = Sprite("targeticon_head.png")
        sprite.rect.x = card.cardsprite.rect.x+240
        sprite.rect.y = card.cardsprite.rect.y+283
        sprites_group.add(sprite)
    if(card.defend[1]):
        sprite = Sprite("targeticon_right_arm.png")
        sprite.rect.x = card.cardsprite.rect.x+232
        sprite.rect.y = card.cardsprite.rect.y+290
        sprites_group.add(sprite)
    if(card.defend[2]):
        sprite = Sprite("targeticon_right_torso.png")
        sprite.rect.x = card.cardsprite.rect.x+235
        sprite.rect.y = card.cardsprite.rect.y+290
        sprites_group.add(sprite)
    if(card.defend[3]):
        sprite = Sprite("targeticon_right_leg.png")
        sprite.rect.x = card.cardsprite.rect.x+232
        sprite.rect.y = card.cardsprite.rect.y+299
        sprites_group.add(sprite)
    if(card.defend[4]):
        sprite = Sprite("targeticon_left_arm.png")
        sprite.rect.x = card.cardsprite.rect.x+248
        sprite.rect.y = card.cardsprite.rect.y+290
        sprites_group.add(sprite)
    if(card.defend[5]):
        sprite = Sprite("targeticon_left_torso.png")
        sprite.rect.x = card.cardsprite.rect.x+243
        sprite.rect.y = card.cardsprite.rect.y+290
        sprites_group.add(sprite)
    if(card.defend[6]):
        sprite = Sprite("targeticon_left_leg.png")
        sprite.rect.x = card.cardsprite.rect.x+245
        sprite.rect.y = card.cardsprite.rect.y+299
        sprites_group.add(sprite)
        
# rendering stuff
def render_card(card):
    sprites_group.add(card.cardsprite)
    sprites_group.add(card.artsprite)
    render_targeticons(card)
    render_defenseicons(card)
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

def resolve(attacker, defender, attack, counter):
    # head, r-arm, r-torso, r-leg, l-arm, l-torso, l-leg
    result = [0,0,0,0,0,0,0]

    for i in range(len(attack.power)):
        result[i] = (counter.defend[i] - attack.power[i])
    for i in range(len(result)):
        defender.health[i] += result[i]
    if(defender.health[0] <= 0 or defender.health[2] <= 0 or defender.health[5] <= 0):
        print("debug_wincondition: " +defender.name + "has died, " + attacker.name + " wins!")
        pygame.display.quit()
        pygame.quit()
        sys.exit()

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
            # ask current player for card
            card = play_card(player)
            if (card):
                if(opener == None):
                    opener = player
                player.stack.append(card)
                if((initiative != player and card.take_initiative == True) or (initiative == player and card.take_initiative == True and opener != player)):
                    # took initiative from opponent, now we evaluate the exchange
                    initiative = player
                    if opener == player1:
                        opponent = player2
                    else:
                        opponent = player1
                    # evaluate each attack of the opener against defense used by opponent
                    print("resolving exchange..")
                    #print("stacksizes: " + str(len(opener.stack)) + ", " + str(len(opponent.stack)))
                    for i in range(len(opener.stack)):
                        #print("resolving: opener[" + str(i) + "], opponent[" + str(i) + "]")
                        resolve(opener, opponent, opener.stack[i], opponent.stack[i])
                        if(i < (len(opener.stack)-1) and (len(opener.stack) > 1)):
                            #print("resolving: opponent[" + str(i) + "], opener[" + str(i+1) + "]")
                            resolve(opponent, opener, opponent.stack[i], opener.stack[i+1])
                    # swap roles, leave the last action of the opponent on his (now opener) stack
                    opener.stack = []
                    leftover = opponent.stack[len(opponent.stack)-1]
                    opponent.stack = []
                    if opener == player1:
                        opener = player2
                        opponent = player1
                    else:
                        opponent = player2
                        opener = player1
                    opener.stack.append(leftover)

                # draw if hand not full
                if (len(player.hand) < 10):
                    player.draw(1)    
                player = hotseat(player)
                if(opener == None):
                    player = initiative
                
    render_player(player)
    # 60 fps glorious pc gaming masterrace
    clock.tick(60)
# out of mainloop, close dis
pygame.quit()
