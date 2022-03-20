from random import shuffle
from time import sleep

# Assign `input` to `raw_input` because we are re-using its name 
raw_input = input

# Handle input
def input(placeholder: str = ""):
    while True:
        try:
            n = raw_input(placeholder)
            break
        except:
            print(
            """
            You are trying to exit the game...
            Press Ctrl-c again to exit
            Or wait 3 seconds to continue.
            """
            )
            sleep(3)
            print("Continuing...")
    return n

# Clear the terminal
def clear():
    os.system('clear')

# Game class
class Game:
    def __init__(self):
        self.playersDeck = []
        self.botsDeck = []

    def start(self):
        '''
        Start a new game
        '''
        ### Initialization
        # Creating decks
        self.playersDeck, self.botsDeck = Deck(), Deck()
        self.cardsPile = Deck()
        self.cardsPile.fill()
        self.cardsPile.shuffle()

        # dealting first two cards
        for times in range(2):
            self.playersDeck.deal(self.cardsPile)
            self.botsDeck.deal(self.cardsPile)

        while not (self.playersDeck.standed or self.playersDeck.busted):
            print(f"You now have {self.playersDeck.points}")
            print(" ".join(self.playersDeck.getRawCards()))
            self.handlePlayer()

        self.handleBot()

    def handlePlayer(self):
        inputs = input("(deal/stand): ").strip().lower()

        if inputs in ["deal", "hit"]:
            self.playersDeck.deal(self.cardsPile)
        elif inputs in ["stand"]:
            self.playersDeck.stand()

        if self.playersDeck.checkIfBusted():
            print("Busted!")

    def handleBot(self):
        deck = self.botsDeck

        if self.playersDeck.busted:
            deck.stand()

        while not (deck.standed or deck.busted):
            print(f"Bot has {deck.points}")
            print(" ".join(deck.getRawCards()))

            if deck.points < 17:
                deck.deal(self.cardsPile)
                print(f"Bot dealed. Bot now has {deck.points}")
            else:
                deck.stand()

            if deck.checkIfBusted():
                print("Busted")

        self.botsDeck = deck

    def checkIfWon(self):
        '''
        Check if anybody won
        '''
        pass

# Card class represent a card
class Card:
    def __init__(self, suit, index, points):
        self.suit = suit
        self.index = index
        self.points = points

    def getSuit(self):
        return self.suit

    def getPoints(self):
        return self.points

    def getRaw(self):
        return f"{self.index}{self.suit}"

# Deck class represent a deck
class Deck:
    def __init__(self):
        self.cards = []
        self.standed = False
        self.busted = False
        self.points = 0

    def fill(self):
        '''
        Fill the deck with cards
        '''
        if len(self.cards) > 0:
            return

        for number in range(1, 13+1):
            card_index = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][number-1]
            card_points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10][number-1]
            for suit in ['♠', '♦', '♣', '♥']:
                card = Card(suit, card_index, card_points)
                self.cards.append(card)

    def pop(self):
        '''
        Remove and return the last element in the deck
        '''
        return self.cards.pop()

    def getRawCards(self):
        '''
        Return list of raw cards which contains suit and its values
        '''
        lst = []
        for card in self.cards:
            lst.append(card.getRaw())
        return lst


    def checkIfBusted(self):
        '''
        Check if this deck busted or not
        '''
        if self.points > 21:
            self.busted = True

        return self.busted


    def deal(self, pile):
        '''
        Deal a card
        '''
        popped_card = pile.pop()
        self.cards.append(popped_card)
        self.points += popped_card.getPoints()

    def stand(self):
        '''
        Stand
        '''
        self.standed = True

    def flush(self):
        '''
        Remove all cards in deck
        '''
        self.cards = []
        self.filled = False

    def shuffle(self):
        '''
        Shuffle the deck randomly
        '''
        shuffle(self.cards)

    def reset(self):
        '''
        Return all values to default
        '''
        self.cards.flush()
        self.points = 0
        self.standed = False
        self.busted = False

    def debug(self):
        '''
        Print all class properties (not meant to be user-friendly)
        '''
        print(self.cards)
        print(self.filled)
        print(self.points)

a = Game()
a.start()