# WORK IN PROGRESS

import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = {
    "1": "Ace",
    "11": "Jack",
    "12": "Queen",
    "13": "King"
}

def get_name(number, array):
    if array.get(str(number)):
        return array[str(number)]
    else:
        return str(number)

def is_consecutive(number):
    return sorted(number) == list(range(min(number), max(number) + 1))

def in_same_suit(cards_array):
    current_suit = ""
    previous_suit = ""
    for card in range(len(cards_array)):
        c = cards_array[card]
        previous_suit = current_suit
        current_suit = c[1]
        if previous_suit != current_suit and previous_suit != "":
            return False
    return True

def get_card_ids(cards_array):
    ids = []
    for card in range(len(cards_array)):
        name = cards_array[card][1]
        if name == "Ace":
            ids.append(1)
        elif name == "Jack":
            ids.append(11)
        elif name == "Queen":
            ids.append(12)
        elif name == "King":
            ids.append(13)
        else:
            ids.append(int(name))
    return ids

def random_card():
    suit = random.randint(0,3)
    rank = random.randint(1,13)
    
    card_info = [
        suits[suit],
        get_name(rank, ranks)
    ]
    
    return card_info

def generate_cards(number):
    cards = []
    for card in range(number):
        cards.append(random_card())
    return cards

def is_royal_flush(cards):
    current_suit = ""
    previous_suit = ""
    types = {
        "10": False,
        "Jack": False,
        "Queen": False,
        "King": False,
        "Ace": False,
    }
    for i in range(len(cards)):
        if (current_suit == previous_suit) or (current_suit == "" or previous_suit == ""):
            previous_suit = current_suit
            current_suit = cards[i][0]
        else:
            return False
        
        if cards[i][1] in types:
            if not types[cards[i][1]]:
                types[cards[i][1]] = True
            else:
                return False
        else:
            return False
    return True

def is_straight_flush(cards_array):
    ids = get_card_ids(cards_array)
    return is_consecutive(ids)
    
def is_four_of_a_kind(cards_array):
    unique_cards = []
    for i in range(len(cards_array)):
        rank = cards_array[i][1]
        found = False
        for entry in unique_cards:
            if entry[0] == rank:
                entry[1] += 1
                found = True
                break
        if not found:
            unique_cards.append([rank, 1])
    if len(unique_cards) == 2:
        if unique_cards[0][1] == 4 or unique_cards[1][1] == 4:
            return True
        else:
            return False
    else:
        return False

def is_full_house(cards_array):
    unique_cards = []
    for i in range(len(cards_array)):
        rank = cards_array[i][1]
        found = False
        for entry in unique_cards:
            if entry[0] == rank:
                entry[1] += 1
                found = True
                break
        if not found:
            unique_cards.append([rank, 1])
    if len(unique_cards) == 2:
        if unique_cards[0][1] == 3 or unique_cards[1][1] == 3:
            return True
        else:
            return False

def get_best_hand(cards_array):
    if is_royal_flush(cards_array):
        return "Royal Flush"
    elif is_straight_flush(cards_array):
        return "Straight Flush"
    elif is_four_of_a_kind(cards_array):
        return "Four of a Kind"
    elif is_full_house(cards_array):
        return "Full House"
    elif is_flush(cards_array):
        return "Flush"
    elif is_straight(cards_array):
        return "Straight"
    elif is_three_of_a_kind(cards_array):
        return "Three of a Kind"
    elif is_two_pair(cards_array):
        return "Two Pair"
    elif is_one_pair(cards_array):
        return "One Pair"
    else:
        return "High Card"

print(is_four_of_a_kind([
    ["", "Ace"], ["", "Ace"], ["", "Ace"], ["", "Ace"], ["", "King"]
]))

print(is_four_of_a_kind([
    ["", "Ace"], ["", "Ace"], ["", "Ace"], ["", "King"], ["", "Queen"]
]))
