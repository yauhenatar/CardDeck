from random import shuffle, choice

OPERATIONS = ['big', 'small']

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
operation = ''

def check_operations(operations=None):
    if operations is None:
        return OPERATIONS


def check_colors(colors=None):
    if colors is None:
        return JOKER_COLORS


def check_suits(suits=None):
    if suits is None:
        return SUITS_LIST


def check_operation():
    global operation
    operations = check_operations()
    operation = input('Enter needed deck (small/big):\n').lower()
    if operation not in operations:
        return check_operation()
    else:
        return operation


def check_cards(operation, cards=None):
    if operation == 'small':
        return STANDART_CARDS
    elif operation == 'big':
        return BIG_CARDS


def create_standart_deck(cards, deck: list):
    suits = check_suits()

    for suit in suits:
        for c in cards:
            deck.append(f'{c} {suit}')

    return deck


def create_big_deck(cards, deck: list):
    suits = check_suits()
    joker_colors = check_colors()

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


def create_deck() -> list:
    deck = list()
    operation = check_operation()
    cards = check_cards(operation)
    if operation == 'small':
        return create_standart_deck(cards, deck)
    elif operation == 'big':
        return create_big_deck(cards, deck)


deck = create_deck()
print(deck)


# def check_deck_len(deck: list):
#     if len(deck)

def get_value(deck: list):
    cards = check_cards(operation)
    card_index = int(input('Enter card number in deck:\n')) - 1
    val = deck[card_index].split()[0]
    for key in cards:
        if val == key:
            return cards[key]


print(get_value(deck))

# shuffle(deck)
#
# for el in deck:
#     for key in BIG_CARDS:
#         if BIG_CARDS[key] == el.split()[0]:
#             deck_values.append(key)
#
# print(deck)
#
# choice_1 = choice(deck)
# choice_2 = choice(deck)
# f_index = deck.index(choice_1)
# s_index = deck.index(choice_2)
#
#
#
# if deck_values[f_index] > deck_values[s_index]:
#     print(f'{choice_1} vs {choice_2}\n'
#           f'Победил {choice_1}')
# elif deck_values[f_index] < deck_values[s_index]:
#     print(f'{choice_1} vs {choice_2}\n'
#           f'Победил {choice_2}')
# else:
#     print(f'{choice_1} vs {choice_2}\n'
#           'Ничья')