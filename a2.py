#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

import random
from abc import ABC

__author__ = "Your name & student number here"

# Write your classes here

class Card:
    def __init__(self, number, colour):
        self._number = number
        self._colour = colour

    def get_number(self):
        '''
        Faker mothafucka on the loose
        '''
        return self._number

    def get_colour(self):
        '''
        Faker mothafucka on the loose
        '''
        return self._colour

    def set_number(self, number):
        '''
        Faker mothafucka on the loose
        '''
        self._number = number

    def set_colour(self, colour):
        '''
        Faker mothafucka on the loose
        '''
        self._colour = colour

    def get_pickup_amount(self):
        '''
        Faker mothafucka on the loose
        '''
        return 0

    def matches(self, card):
        '''
        Faker mothafucka on the loose
        '''
        if card.get_number() == self._number or card.get_colour() == self._colour:
            return True
        return False
    def play(self, player, game):
        '''
        Faker mothafucka on the loose
        '''
        pass

    def __str__(self):
        return 'Card({}, {})'.format(self._number, self._colour)

    __repr__ = __str__



class SkipCard(Card):
    def __init__(self, number, colour):
        self._number = number
        self._colour = colour

    def get_pickup_amount(self):
        return 0

    def play(self, player, game):
        while player.get_name() != game.current_player().get_name():
            game.next_player()
        game.skip()

    def __str__(self):
        return 'SkipCard({}, {})'.format(self._number, self._colour)

    __repr__ = __str__

class ReverseCard(Card):
    def __init__(self, number, colour):
        self._number = number
        self._colour = colour

    def get_pickup_amount(self):
        return 0

    def play(self, player, game):
        game.reverse()

    def __str__(self):
        return 'ReverseCard({}, {})'.format(self._number, self._colour)

    __repr__ = __str__

class Pickup2Card(Card):
    def __init__(self, number, colour):
        self._number = number
        self._colour = colour

    def get_pickup_amount(self):
        return 2

    def play(self, player, game):
        while player.get_name() != game.current_player().get_name():
            game.next_player()
        game.get_turns().peak().get_deck().add_cards(game.pickup_pile.pick(2))

    def __str__(self):
        return 'Pickup2Card({}, {})'.format(self._number, self._colour)

    __repr__ = __str__


class Pickup4Card(Card):
    def __init__(self, number, colour):
        self._number = number
        self._colour = colour

    def get_pickup_amount(self):
        return 4

    def matches(self,card):
        return True

    def play(self, player, game):
        while player.get_name() != game.current_player().get_name():
            game.next_player()
        game.get_turns().peak().get_deck().add_cards(game.pickup_pile.pick(4))

    def __str__(self):
        return 'Pickup4Card({}, {})'.format(self._number, self._colour)

    __repr__ = __str__


class Deck:
    def __init__(self, starting_cards=None):
        if not starting_cards:
            starting_cards = []
        self._cards = starting_cards

    def get_cards(self):
        '''
        Faker mothafucka on the loose
        '''
        return self._cards

    def get_amount(self):
        '''
        Faker mothafucka on the loose
        '''
        return len(self._cards)

    def shuffle(self):
        '''
        Faker mothafucka on the loose
        '''
        random.shuffle(self._cards)

    def pick(self, amount=1):
        '''
        Faker mothafucka on the loose
        '''
        picked_card_list = []
        while amount > 0:
            picked_card_list.append(self._cards.pop())
            amount -= 1
        return picked_card_list

    def add_card(self, card):
        '''
        Faker mothafucka on the loose
        '''
        self._cards.append(card)

    def add_cards(self, cards):
        '''
        Faker mothafucka on the loose
        '''
        self._cards.extend(cards)

    def top(self):
        '''
        Faker mothafucka on the loose
        '''
        return self._cards[-1]

class Player(ABC):
    def __init__(self, name):
        self._name = name
        self._deck = Deck()

    def get_name(self):
        '''
        Faker mothafucka on the loose
        '''
        return self._name

    def get_deck(self):
        '''
        Faker mothafucka on the loose
        '''
        return self._deck

    def is_playable(self):
        '''
        Faker mothafucka on the loose
        '''
        raise NotImplementedError()

    def has_won(self):
        '''
        Faker mothafucka on the loose
        '''
        if self._deck.get_amount() == 0:
            return True
        return False

    def pick_card(self, putdown_pile):
        '''
        Faker mothafucka on the loose
        '''
        raise NotImplementedError()


class HumanPlayer(Player):
    def is_playable(self):
        return True

    def pick_card(self, putdown_pile):
        return None

class ComputerPlayer(Player):
    def is_playable(self):
        return False

    def pick_card(self, putdown_pile):
        if putdown_pile:
            for card in self._deck.get_cards():
                if card.matches(putdown_pile.top()):
                    self._deck.get_cards().remove(card)
                    return card
        else:
            card = random.choice(self._deck.get_cards())
            self._deck.get_cards().remove(card)
            return card

def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
