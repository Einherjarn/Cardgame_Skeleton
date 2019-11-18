import pygame
import random
import pygame.freetype
from sprite import Sprite
from card_base import Card_base

def strbool(s):
    if s.lower()=="true":
        return True
    else:
        return False

# loads card of given name into actual card object
def load_card(name, card, player):
    if name:
        # card parser
        f= open("card_data.txt", "r")
        stuff = f.readlines()
        f.close()
        for i in range(len(stuff)):
            line = stuff[i].split()
            """for j in range(len(line)):
                print(line[j], j)"""
            if(len(line) > 0):
                if line[0].strip()==name.strip():
                    #convert name from _ to spaces
                    name = line[0].strip()
                    newname = ""
                    for i in name:
                        if i=="_":
                            newname +=" "
                        else:
                            newname +=i
                    card.name = newname
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
                    newdesc = ""
                    for i in description:
                        if i=="_":
                            newdesc +=" "
                        else:
                            newdesc +=i

                    card.description = newdesc

        # modifier parser
        f=open("modifiers.txt")
        stuff = f.readlines()
        f.close()
        for i in range(len(stuff)):
            if(stuff[i].strip() == name):
                for j in range(i,len(stuff)):
                    if(stuff[j].strip()=="end"):
                        end = j
                        break
                #print(str(i+1) +", " +str(end-1))
                for k in range(i+1,end-1):
                    line = stuff[k].split()
                    newmod = []
                    newmod.append(line[0].strip())
                    newmod.append(line[1].strip())
                    newmod.append(player)
                    for l in range(2,len(line)):
                        newmod.append(int(line[l].strip()))
                    card.modifiers.append(newmod)
        """for i in range(len(card.modifiers)):
            for j in range(len(card.modifiers[i])):
                print(card.modifiers[i][j])"""




# loads deck of given name into given list
def load_deck(name, deck, player):
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
                else:
                    break
            if i.strip()==name:
                found = True

        for i in range(len(cardnames)):
            deck.append(Card_base())
            load_card(cardnames[i], deck[i], player)

        """print("loading deck: " +name)
        for i in deck:
            print(i.name)"""



class Player:
    def __init__(self, deckname, playername):
        self.name = playername
        """Hits follows the format of
        head, right arm, right torso, right leg, left arm, left torso, left leg"""
        self.health = [2,2,2,2,2,2,2]
        """stats are strength, quickness, foresight and fortitution"""
        self.stats = [0,0,0,0]
        self.deck = []
        load_deck(deckname,self.deck,self)
        self.hand = []
        self.discardpile = []
        self.stack = []
        self.prompt = []
        self.drew = False
        """presuming 10 stamina is max"""
        self.stamina = 10
        """Force player to choose a stance, then put stance here"""
        self.stance = None
        self.invulnerable = [False, False, False, False, False, False, False]

    """draw n cards from deck"""
    def draw(self, n):
        if(len(self.deck) >= n):
            for i in range(n):
                self.hand.append(self.deck.pop())
        elif(len(self.deck) > 0):
            for i in range(len(self.deck)):
                self.hand.append(self.deck.pop())
    def shuffle(self):
        rng = random.SystemRandom()
        random.shuffle(self.deck, rng.random)

    """discard a card at index i"""
    def discard(self, i):
        self.discardpile.append(self.hand.pop(i))

    def setStance(self):
        pass
