from random import choice
from config import *


def set_deck_length(deck_length=None):
    if deck_length is None or deck_length == '':
        return DECK_LENGTH


def set_suits(suits=None):
    if suits is None:
        return SUITS_LIST


def get_deck_type() -> str:
    operations = set_deck_length()
    operation = input('Enter needed deck (small/big):\n').lower()
    if operation not in operations:
        return get_deck_type()
    else:
        return operation


def set_cards(deck_length):
    return SMALL_DECK if deck_length == 'small' else BIG_DECK


def create_small_deck(cards):
    deck = list()
    suits = set_suits()

    for suit in suits:
        for c in cards:
            deck.append(f'{cards[c]} {suit}')

    return deck


def create_big_deck(cards, colors=None):
    deck = list()
    suits = set_suits()
    if colors is None:
        colors = JOKER_COLORS

    for color in colors:
        for jc in cards:
            if cards[jc] == 'joker':
                deck.append(f'{cards[jc]} {color}')

    for suit in suits:
        for c in cards:
            if cards[c] != 'joker':
                deck.append(f'{cards[c]} {suit}')

    return deck


def create_deck():
    operation = get_deck_type()
    cards = set_cards(operation)
    return create_small_deck(cards) if operation == 'small' else create_big_deck(cards)


def get_value(card: str):
    cards = set_cards(deck_length)
    num_card = card.split()[0]
    for key in cards:
        if num_card == cards[key]:
            return key


def get_num_cards_to_play():
    return int(input('Enter count of playing cards:\n'))


def took_random_cards(deck: list):
    cards_to_play = get_num_cards_to_play()
    cards_list = list()
    for i in range(cards_to_play):
        choosed = choice(deck)
        cards_list.append(choosed)
        deck.remove(choosed)
    return cards_list


def get_values_of_random_cards(random_cards: list):
    values_list = list()
    for card in random_cards:
        values_list.append(get_value(card))
    return values_list


def get_winners(random_cards: list):
    values_cards = get_values_of_random_cards(random_cards)
    max_value = max(values_cards)
    print('WINNER(S):')
    for el_rand, el_val in zip(random_cards, values_cards):
        if max_value == el_val:
            print(el_rand)


if __name__ == '__main__':
    deck_length = ''
    deck = create_deck()
    random_cards = took_random_cards(deck)
    get_winners(random_cards)
