from enum import Enum
import random


class Suite(Enum):
    SPADE = 0
    HEART = 1
    DIAMOND = 2
    CLUB = 3


class Card:
    def __init__(self, number, suite: Suite) -> None:
        self.number = number
        self.suite = suite

    def show_card(self):
        print(f"{self.number} of  {self.suite.name}")


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.build_deck()

    def build_deck(self):

        for suite in Suite:
            for i in range(1, 14):
                self.cards.append(Card(i, suite))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)

            self.cards[r], self.cards[i] = self.cards[i], self.cards[r]

    def show(self):
        for c in self.cards:
            c.show_card()

    def draw(self):
        return self.cards.pop()


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = []

    def draw(self, deck):
        card = deck.draw()
        self.hand.append(card)
        return self

    def show_hand(self):
        for card in self.hand:
            card.show_card()


if __name__ == "__main__":

    deck = Deck()
    deck.shuffle()
    deck.show()
    print("######################")
    player = Player("Ayan")
    player.draw(deck).draw(deck)
    player.show_hand()
