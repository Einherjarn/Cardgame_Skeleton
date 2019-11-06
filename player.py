class Player:
    def __init__(self, deck):
        """Hits follows the format of
        head, right arm, right torso, right leg, left arm,
        left torso, left leg"""
        self.hits[False,False,False,False,False,False,False]
        """stats are strength, quickness, foresight and fortitution
        in that order"""
        self.stats[0,0,0,0]
        self.deck = deck
        self.hand = []
        self.discard = []
        """presuming 10 stamina is max"""
        self.stamina = 10
        """Force player to choose a stance, then put stance here"""
        self.stance = None

    """draw n cards from deck"""
    def draw(self, n):
        for i in range(n):
            hand.append(deck.pop())
    """set stat m to n where n =/= 0"""
    def setStat(self,n,m):
        stats[m] = n
    """get stat n"""
    def getstat(self,n):
        return stats[n]

    def shuffle(self):
        """code"""

    """discard n cards"""
    def discard(self, n):
        """code"""

    def setMana(self, n):
        """code"""

    def getMana(self):
        """code"""

    def getHits(self):
        """code"""
        
    """set hit to index n to true"""
    def setHits(self, n):
        """code"""
