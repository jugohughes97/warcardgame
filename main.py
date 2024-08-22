import random

class CardGame:

    def __init__(self):

        self.deck = DeckOfCards()
        self.deck.shuffle_deck()


    def play(self):

        print("Nothing to play...")


class War(CardGame):

    def __init__(self):

        super().__init__()
        self.player1_hand = []
        self.player2_hand = []


    def play(self):

        for card in self.__deal_hand():
            
            self.player1_hand.append(card)
        for card in self.__deal_hand():
            
            self.player2_hand.append(card)
        self.__battle()


    def __deal_hand(self):
        
        hand = []
        for i in range(0, 5):
            
            hand.append(self.deck.deal_card())
        return hand


    def __battle(self):

        player1_pile = []
        player2_pile = []
        player1_score = 0
        player2_score = 0
        ties = 0

        while len(self.player1_hand) > 0 or len(self.player2_hand) > 0:
            
            if len(self.player1_hand) == 0:
                
                random.shuffle(player1_pile)
                self.player1_hand = player1_pile.copy()
                player1_pile.clear()
            if len(self.player2_hand) == 0:

                random.shuffle(player2_pile)
                self.player2_hand = player2_pile.copy()
                player2_pile.clear()
            card1 = self.player1_hand.pop()
            card2 = self.player2_hand.pop()
            print(f"{card1} vs {card2}")
            
            if card1 > card2:

                player1_pile.append(card1)
                player1_pile.append(card2)
                player1_score += 1
                print(f"Player 1 wins with {card1}")
            elif card2 > card1:

                player2_pile.append(card1)
                player2_pile.append(card2)
                player2_score += 1
                print(f"Player 2 wins with {card2}")
            else:

                ties += 1
                print("Tie! Both players draw a card and play again")
        
        print("------------------------------------------")
        print("Game over!")
        print("------------------------------------------")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")
        print(f"Ties: {ties}")
        print("==========================================")


SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Card:

    def __init__(self, rank, suit):

        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)


    def __eq__(self, other):

        return self.rank_index == other.rank_index and self.suit_index == other.suit_index


    def __gt__(self, other):

        return (self.rank_index > other.rank_index or 
                (self.suit_index > other.suit_index and self.rank_index == other.rank_index)
               )


    def __lt__(self, other):

        return (self.rank_index < other.rank_index or 
                (self.suit_index < other.suit_index and self.rank_index == other.rank_index)
               )


    def __str__(self):
        return f"{RANKS[self.rank_index]} of {SUITS[self.suit_index]}"


class DeckOfCards:

    def __init__(self):

        self.__cards = []
        self.create_deck()


    def create_deck(self):

        for suit in SUITS:

            for rank in RANKS:

                self.__cards.append(Card(rank, suit))


    def shuffle_deck(self):

        random.shuffle(self.__cards)


    def deal_card(self):

        if len(self.__cards) == 0:
            
            return None
        return self.__cards.pop(0)



def main():
    random.seed()
    war = War()
    war.play()

main()
