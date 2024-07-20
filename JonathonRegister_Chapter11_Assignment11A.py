import random


# Define Card and Deck classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        # creates the entire deck of cards
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def draw(self, num_cards):
        drawn_cards = []
        for _ in range(num_cards):
            drawn_cards.append(self.cards.pop())
        return drawn_cards


# Function to print current hand
def print_hand(hand):
    for i, card in enumerate(hand):
        print(f"{i + 1}: {card}")


# Main function to play the game
def play_poker():
    # creates the hand for the user
    deck = Deck()
    hand = deck.draw(5)

    print("Your current hand:")
    print_hand(hand)

    # user input to replace which cards they want, and then re-shuffles for new cards to replace user's input
    replace_indices = input("Enter the positions of cards to replace (e.g., 1, 3, 5): ")
    replace_indices = list(map(int, replace_indices.split(',')))

    for idx in replace_indices:
        hand[idx - 1] = deck.draw(1)[0]

    print("\nYour new hand after replacement:")
    print_hand(hand)


# Main execution
if __name__ == "__main__":
    play_poker()
