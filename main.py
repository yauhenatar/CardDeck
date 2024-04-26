from random import choice

DECK_LENGTH = ['big', 'small']

STANDART_CARDS = {
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'jack': 11,
    'queen': 12,
    'king': 13,
    'ace': 14
}

BIG_CARDS = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'jack': 11,
    'queen': 12,
    'king': 13,
    'ace': 14,
    'joker': 15
}

SUITS_LIST = ['hearts', 'clubs', 'spades', 'diamonds']
JOKER_COLORS = ['black', 'red']

deck_values = list()
deck_length = ''


def set_deck_length(deck_length=None):
    if deck_length is None:
        return DECK_LENGTH


def set_colors(colors=None):
    if colors is None:
        return JOKER_COLORS


def set_suits(suits=None):
    if suits is None:
        return SUITS_LIST


def set_deck_lenght():
    global deck_length
    operations = set_deck_length()
    operation = input('Enter needed deck (small/big):\n').lower()
    if operation not in operations:
        return set_deck_lenght()
    else:
        return operation


def set_cards(deck_length):
    if deck_length == 'small':
        return STANDART_CARDS
    elif deck_length == 'big':
        return BIG_CARDS


def create_standart_deck(cards, deck: list):
    suits = set_suits()

    for suit in suits:
        for c in cards:
            deck.append(f'{c} {suit}')

    return deck


def create_big_deck(cards, deck: list):
    suits = set_suits()
    joker_colors = set_colors()

    for color in joker_colors:
        for jc in cards:
            if jc == 'joker':
                deck.append(f'{jc} {color}')

    for suit in suits:
        for c in cards:
            if c == 'joker':
                pass
            else:
                deck.append(f'{c} {suit}')

    return deck


def create_deck():
    deck = list()
    operation = set_deck_lenght()
    cards = set_cards(operation)
    if operation == 'small':
        return create_standart_deck(cards, deck)
    elif operation == 'big':
        return create_big_deck(cards, deck)


def get_value(card: str):
    cards = set_cards(deck_length)
    num_card = card.split()[0]
    for key in cards:
        if num_card == key:
            return cards[key]


def set_num_cards_to_play():
    return int(input('Enter count of playing cards:\n'))


def took_random_cards(deck: list):
    cards_to_play = set_num_cards_to_play()
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
    max_index = values_cards.index(max_value)
    for i in range(len(random_cards)):
        if max_value not in values_cards:
            break
        else:
            print(random_cards[max_index])
            del values_cards[max_index]
            del random_cards[max_index]

