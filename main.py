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
size = (960,800)
screen = pygame.display.set_mode(size)

font_cardname = pygame.freetype.Font(None, 14)
font_health = pygame.freetype.Font(None, 16)
font_description = pygame.freetype.Font(None, 18)
font_stamcost = pygame.freetype.Font(None, 36)
font_prompt = pygame.freetype.Font(None, 36)
font_stamina = pygame.freetype.Font(None, 42)
font_cardselection = pygame.freetype.Font(None, 42)
font_playername = pygame.freetype.Font(None, 42)

pygame.display.set_caption("cardgame skeleton")
sprites_group = pygame.sprite.Group()
Continue = True
clock = pygame.time.Clock()
click = pygame.time.get_ticks()

player1 = Player("dev_testing_deck_longsword", "player 1")
player1.shuffle()
player2 = Player("dev_testing_deck_longsword", "player 2")
player2.shuffle()

# variables used in handling gamestate
initiative = None
opener = None
opponent = None
skip_playcard = False
swap = False
card = None
resolving = 0

def run_arbitrary(name, args):
    """print("debug, run_arbitrary(" + name +", [])")
    for i in range(len(args)):
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
    try:
        return card
    except NameError:
        return

def pick_card(player):
    global click
    render_player(player)
    (b1,b2,b3) = pygame.mouse.get_pressed()
    if(b1 > 0 and (pygame.time.get_ticks() - 100 > click) and event.type == pygame.MOUSEBUTTONDOWN):
        card = card_on_mouse(player)
        click = pygame.time.get_ticks()
        if(card != None):
            print(card.name)
            return card
        else:
            return

def play_card(player):
    global click
    render_player(player)
    (b1,b2,b3) = pygame.mouse.get_pressed()
    if(b1 > 0 and (pygame.time.get_ticks() - 100 > click) and event.type == pygame.MOUSEBUTTONDOWN):
        card = card_on_mouse(player)
        click = pygame.time.get_ticks()
        if(card != None):
            # find and execute possible OnPlay modifiers
            for i in range(len(card.modifiers)):
                if(card.modifiers[i][1] == "OnPlay"):
                    args = []
                    for j in range(2,len(card.modifiers[i])):
                        args.append(card.modifiers[i][j])
                    args.append(player1)
                    args.append(player2)
                    run_arbitrary(card.modifiers[i][0],args)
                    print(player.name)
            print(card.name)
            player.discard(player.hand.index(card))
            return card
        else:
            return

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
        sprite.rect.x = card.cardsprite.rect.x+235
        sprite.rect.y = card.cardsprite.rect.y+256
        sprites_group.add(sprite)
    if(card.target[3]):
        sprite = Sprite("targeticon_right_leg.png")
        sprite.rect.x = card.cardsprite.rect.x+232
        sprite.rect.y = card.cardsprite.rect.y+266
        sprites_group.add(sprite)
    if(card.target[4]):
        sprite = Sprite("targeticon_left_arm.png")
        sprite.rect.x = card.cardsprite.rect.x+248
        sprite.rect.y = card.cardsprite.rect.y+257
        sprites_group.add(sprite)
    if(card.target[5]):
        sprite = Sprite("targeticon_left_torso.png")
        sprite.rect.x = card.cardsprite.rect.x+245
        sprite.rect.y = card.cardsprite.rect.y+258
        sprites_group.add(sprite)
    if(card.target[6]):
        sprite = Sprite("targeticon_left_leg.png")
        sprite.rect.x = card.cardsprite.rect.x+245
        sprite.rect.y = card.cardsprite.rect.y+266
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
        sprite.rect.y = card.cardsprite.rect.y+289
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
        sprite.rect.y = card.cardsprite.rect.y+289
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
    global swap
    if (swap == False):
        if player == player1:
            otherplayer = player2
        else:
            otherplayer = player1
        # define positions of cards, in 2 rows if more than 5
        for i in range(len(player.hand)):
            # basic sine wave for cards held in hand
            heightmod = 50 * (-1 * math.sin((i+0.5)/1.51))
            if (player.hand[i] and i < 5):
                player.hand[i].cardsprite.rect.x = 50+(i*150)
                player.hand[i].cardsprite.rect.y = 500+(heightmod)
                player.hand[i].artsprite.rect.x = 50+(i*150)+3
                player.hand[i].artsprite.rect.y = 500+(heightmod)+3
            elif (player.hand[i]):
                player.hand[i].cardsprite.rect.x = 50+((i-5)*150)
                player.hand[i].cardsprite.rect.y = 550+(heightmod-5)
                player.hand[i].artsprite.rect.x = 50+((i-5)*150)+3
                player.hand[i].artsprite.rect.y = 550+(heightmod-5)+3
            
        # individual screen elements
        if(player.prompt != []):
            font_prompt.render_to(screen, (400,10), player.prompt[0], (0, 0, 0))
        font_stamina.render_to(screen, (120,10), str(player.stamina), (0, 255, 0))
        font_playername.render_to(screen, (120,50), str(player.name), (0, 0, 0))
        cardonmouse = card_on_mouse(player) 
        if (cardonmouse):
            cardonmouse.cardsprite.rect.y -= 100
            cardonmouse.artsprite.rect.y -= 100
            font_cardselection.render_to(screen, (120,100), cardonmouse.name, (0, 0, 0))

        # add all card sprites to spritegroup
        screen.fill((200,200,200))
        for i in range(len(player.hand)):
            render_card(player.hand[i])

        # render selected card over others
        if (cardonmouse):
            render_card(cardonmouse)

        # render last card played by opponent so we see what were responding to
        if(len(otherplayer.stack) > 0):
            op_stacktop = otherplayer.stack[len(otherplayer.stack)-1]
            op_stacktop.cardsprite.rect.x = 525
            op_stacktop.cardsprite.rect.y = 10
            op_stacktop.artsprite.rect.x = 525+3
            op_stacktop.artsprite.rect.y = 10+3
            render_card(op_stacktop)
        # health indicators
            # current player
        font_playername.render_to(screen, (10,200), str(player.name), (0, 0, 0))
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

            # opponent
        player = otherplayer
        font_playername.render_to(screen, (800,200), str(player.name), (0, 0, 0))
        playersprite = Sprite("player_status_image.png")
        playersprite.rect.x = 850
        playersprite.rect.y = 5
        sprites_group.add(playersprite)
        sprites_group.update()
        sprites_group.draw(screen)
        sprites_group.empty()
        #head
        font_health.render_to(screen, (900,15), str(player.health[0]), (255, 0, 0))
        #r-arm
        font_health.render_to(screen, (855,50), str(player.health[1]), (255, 0, 0))
        #r-torso
        font_health.render_to(screen, (885,50), str(player.health[2]), (255, 0, 0))
        #r-leg
        font_health.render_to(screen, (885,160), str(player.health[3]), (255, 0, 0))
        #l-arm
        font_health.render_to(screen, (945,50), str(player.health[4]), (255, 0, 0))
        #l-torso
        font_health.render_to(screen, (915,50), str(player.health[5]), (255, 0, 0))
        #l-leg
        font_health.render_to(screen, (915,160), str(player.health[6]), (255, 0, 0)) 
    else:
        screen.fill((0,0,0))
        font_prompt.render_to(screen, (40,40), player.name +" please click to continue.", (255, 255, 255))
    # updating screen
    pygame.display.flip()

# swap player in seat
def hotseat(player):
    global swap
    if(swap == False):
        swap = True
    if(player == player1):
        player = player2
    else:
        player = player1
    return player

def resolve(attacker, defender, attack, counter):
    # head, r-arm, r-torso, r-leg, l-arm, l-torso, l-leg
    result = [0,0,0,0,0,0,0]
    deflect = True

    for i in range(len(attack.power)):
        result[i] = (counter.defend[i] - attack.power[i])
        if (result[i] > 0):
            deflect = False
    for i in range(len(result)):
        if(result[i] < 0):
            defender.health[i] += result[i]
    
    # find and execute possible OnDeflect modifiers
    if (deflect == True):
        for i in range(len(attack.modifiers)):
            if(attack.modifiers[i][1] == "OnDeflect"):
                args = []
                for j in range(2,len(attack.modifiers[i])):
                    args.append(attack.modifiers[i][j])
                args.append(player1)
                args.append(player2)
                run_arbitrary(attack.modifiers[i][0],args)
        # find and execute possible OnDefend modifiers
        for i in range(len(counter.modifiers)):
            if(counter.modifiers[i][1] == "OnDefend"):
                args = []
                for j in range(2,len(counter.modifiers[i])):
                    args.append(counter.modifiers[i][j])
                args.append(player1)
                args.append(player2)
                run_arbitrary(counter.modifiers[i][0],args)
    # find and execute possible OnHit modifiers
    else:
        for i in range(len(attack.modifiers)):
            if(attack.modifiers[i][1] == "OnHit"):
                args = []
                for j in range(2,len(attack.modifiers[i])):
                    args.append(attack.modifiers[i][j])
                args.append(player1)
                args.append(player2)
                run_arbitrary(attack.modifiers[i][0],args)
    
    if(defender.health[0] <= 0 or defender.health[2] <= 0 or defender.health[5] <= 0):
        print("debug_wincondition: " +defender.name + " has died, " + attacker.name + " wins!")
        pygame.display.quit()
        pygame.quit()
        sys.exit()

def process_prompt(player, player1, player2):
    # top prompt is for a card
    if(player.prompt[0] == "Pick a card"):
        card = pick_card(player)
        if(card):
            args = []
            args.append(player)
            args.append(player.hand.index(card))
            args.append(player1)
            args.append(player2)
            run_arbitrary(player.prompt[1],args)
            player.prompt.pop(0)
            player.prompt.pop(0)
                

def iterate_game():
    global player, player1, player2, initiative, opener, opponent, resolving, skip_playcard, card, swap, click
    """print(str(player) +str(player1) +str(player2))
    print(str(initiative) +str(opener) +str(opponent))
    print(str(resolving))"""
    if(swap == False):
        if player == player1:
            otherplayer = player2
        else:
            otherplayer = player1
        # current player has no prompts
        if(player.prompt == []):
            if(opener == None):
                opes = 0
            else:
                opes = len(opener.stack)
            if(opponent == None):
                opps = 0
            else:
               opps = len(opponent.stack)
            # we were previously resolving stacks
            #print(str(resolving) +", " +str(opes) +", " +str(opps))
            if(resolving < (opes + opps - 1)):
                print("resolving exchange..")
                #print("stacksizes: " + str(len(opener.stack)) + ", " + str(len(opponent.stack)) + "; resolve iteration: " +str(resolving))
                # we are resolving odd iteration, meaning opener move
                if((resolving % 2) != 0 or resolving == 0):
                    #print("resolving: opener[" + str(resolving) + "], opponent[" + str(resolving) + "]")
                    resolve(opener, opponent, opener.stack[resolving], opponent.stack[resolving])
                    resolving += 1
                # we are resolving even iteration, meaning opponent move
                else:
                    #print("resolving: opponent[" + str(resolving) + "], opener[" + str(resolving+1) + "]")
                    resolve(opponent, opener, opponent.stack[resolving], opener.stack[resolving+1])
                    resolving += 1
            # playing a new card, expected primary route of logic
            else:
                if(skip_playcard == False):
                    # draw if hand not full and we havent drawn yet this turn
                    if (len(player.hand) < 10 and player.drew == False):
                        player.draw(1)
                    player.drew = True
                    # ask current player for card
                    card = play_card(player)
                # card did not create prompt
                if(player.prompt == []):
                    if(card):
                        if(card.take_initiative == True):
                            initiative = player
                        # if this was the first card played in an exchange
                        if(opener == None):
                            opener = player
                            opponent = otherplayer
                        player.stack.append(card)
                        card = None
                        skip_playcard = False
                        player.drew = False
                        player = hotseat(player)
                # newly played card caused a prompt       
                else:
                    if(card):
                        skip_playcard = True
                    return
            # we have resolved both stacks
            if((resolving >= (opes + opps -1)) and resolving > 0 and opener != None and opponent != None):
                print("resolved both stacks")
                resolving = 0
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

        # current player has prompts
        elif(len(player.prompt) > 0):
            process_prompt(player, player1, player2)
        # other player has prompts
        elif(len(otherplayer.prompt) > 0):
            process_prompt(otherplayer, player2, player2)
    else:
        # wait on black screen for new player to acknowledge seat swap
        (b1,b2,b3) = pygame.mouse.get_pressed()
        if(b1 > 0 and (pygame.time.get_ticks() - 100 > click) and event.type == pygame.MOUSEBUTTONDOWN):
            click = pygame.time.get_ticks()
            swap = False
       

# Main Program Logic Loop
while Continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False
        else:
            pass
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

    # process one step of game logic
    iterate_game()
    render_player(player)
    # 60 fps glorious pc gaming masterrace
    clock.tick(60)
# out of mainloop, close dis
pygame.quit()
