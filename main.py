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
pygame.display.set_caption("cardgame skeleton")
sprites_group = pygame.sprite.Group()
Continue = True
clock = pygame.time.Clock()
spritelist = []

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

def strbool(s):
    if s.lower()=="true":
        return True
    else:
        return False

# loads card of given name into actual card object
def load_card(name, card):
    if name:
        f= open("card_data.txt", "r")
        stuff = f.readlines()
        f.close()
        for i in range(len(stuff)):
            line = stuff[i].split()
            """for j in range(len(line)):
                print(line[j], j)"""
            if line[0].strip()==name.strip():
                card.name = line[0].strip()
                card.artsprite = Sprite(line[1].strip())
                card.basecost = int(line[2].strip())
                card.range = int(line[3].strip())
                for i in range(len(card.target)):
                    card.target[i] = strbool(line[i+4].strip())
                for i in range(len(card.defend)):
                    card.defend[i] = strbool(line[i+11].strip())
                for i in range(len(card.power)):
                    card.power[i] = int(line[i+18].strip())
                for i in range(len(card.defense_power)):
                    card.defense_power[i] = int(line[i+25].strip())
                card.take_initiative = strbool(line[32].strip())
                #convert description from _ to spaces
                description = line[33].strip()
                for i in range(len(description)):
                    if i=="_":
                        i=" "
                card.description = description
                #if there are any modifiers
                for i in range(0,len(line)-34,2):
                    card.modifiers.append(line[34+i])
                    card.modifiers.append(line[34+i+1])
    

# loads deck of given name into given list
def load_deck(name, deck):
    if name:
        f= open("deck_data.txt", "r")
        stuff = f.readlines()
        f.close()
        
        found = False
        cardnames = []
        
        for i in stuff:
            if found:
                if i.strip()!="end_deck":
                    cardnames.append(i)
            if i.strip()==name:
                found = True

        for i in range(len(cardnames)):
            deck.append(Card_base())
            load_card(cardnames[i], deck[i])
        """
        for i in deck:
            print(i)
        """

player1turn = True
player1deck = []
player1 = Player(load_deck("dev_testing_deck_longsword",player1deck))
player2deck = []
player2 = Player(load_deck("dev_testing_deck_longsword",player2deck))

# Main Program Logic Loop
while Continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False
    # all primary game logic goes under here, before the rendering stuff
    if player1turn:
        for i in range(5):
            if player1deck[i]:
                player1deck[i].cardsprite.rect.x = 100+(i*150)
                player1deck[i].cardsprite.rect.y = 350
                player1deck[i].artsprite.rect.x = 100+(i*150)+3
                player1deck[i].artsprite.rect.y = 350+3
                spritelist.append(player1deck[i].cardsprite)
                spritelist.append(player1deck[i].artsprite)
    # add all card sprites to spritegroup
    for i in range(len(spritelist)):
        sprites_group.add(spritelist[i])
    
    sprites_group.update()
    screen.fill((200,200,200))
    
    sprites_group.draw(screen)

    for i in range(len(spritelist),2):
        font_description.render_to(screen, (player1deck[i].cardsprite.rect.x+20, player1deck[i].cardsprite.rect.y+165), player1deck[i].description, (0, 0, 0))
        font_stamcost.render_to(screen, (player1deck[i].cardsprite.rect.x+10, player1deck[i].cardsprite.rect.y+10), str(player1deck[i].basecost), (0, 255, 0))
    # updating screen
    pygame.display.flip()

    # 60 fps glorious pc gaming masterrace
    clock.tick(60)
# out of mainloop, close dis
pygame.quit()
