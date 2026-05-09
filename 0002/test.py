import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import testutils
import solution

def make_hand(cards):
    return [[suit, rank] for suit, rank in cards]

testutils.Test.assert_equals(
    solution.get_name(1, solution.ranks),
    "Ace",
    "get_name() - Ace"
)

testutils.Test.assert_equals(
    solution.get_name(7, solution.ranks),
    "7",
    "get_name() - Normal Number"
)

testutils.Test.assert_equals(
    solution.is_consecutive([1, 2, 3, 4, 5]),
    True,
    "is_consecutive() - Normal Straight"
)

testutils.Test.assert_equals(
    solution.is_consecutive([10, 11, 12, 13, 1]),
    True,
    "is_consecutive() - Royal Straight"
)

testutils.Test.assert_equals(
    solution.is_consecutive([1, 2, 2, 4, 5]),
    False,
    "is_consecutive() - Duplicate Values"
)

testutils.Test.assert_equals(
    solution.is_consecutive([1, 3, 4, 5, 6]),
    False,
    "is_consecutive() - Broken Sequence"
)

same_suit_hand = make_hand([
    ("Hearts", "2"),
    ("Hearts", "5"),
    ("Hearts", "7"),
    ("Hearts", "9"),
    ("Hearts", "King"),
])

mixed_suit_hand = make_hand([
    ("Hearts", "2"),
    ("Spades", "5"),
    ("Hearts", "7"),
    ("Hearts", "9"),
    ("Hearts", "King"),
])

testutils.Test.assert_equals(
    solution.in_same_suit(same_suit_hand),
    True,
    "in_same_suit() - Same Suit"
)

testutils.Test.assert_equals(
    solution.in_same_suit(mixed_suit_hand),
    False,
    "in_same_suit() - Mixed Suits"
)

ids_hand = make_hand([
    ("Hearts", "Ace"),
    ("Spades", "10"),
    ("Clubs", "Jack"),
    ("Diamonds", "Queen"),
    ("Hearts", "King"),
])

testutils.Test.assert_equals(
    solution.get_card_ids(ids_hand),
    [1, 10, 11, 12, 13],
    "get_card_ids()"
)

random_card = solution.random_card()

valid_suit = random_card[0] in solution.suits
valid_rank = (
    random_card[1] in solution.ranks.values()
    or random_card[1].isdigit()
)

testutils.Test.assert_equals(
    valid_suit and valid_rank,
    True,
    "random_card()"
)

generated = solution.generate_cards(5)

testutils.Test.assert_equals(
    len(generated),
    5,
    "generate_cards() - Correct Length"
)

royal_flush = make_hand([
    ("Hearts", "10"),
    ("Hearts", "Jack"),
    ("Hearts", "Queen"),
    ("Hearts", "King"),
    ("Hearts", "Ace"),
])

straight_flush = make_hand([
    ("Spades", "5"),
    ("Spades", "6"),
    ("Spades", "7"),
    ("Spades", "8"),
    ("Spades", "9"),
])

four_kind = make_hand([
    ("Hearts", "9"),
    ("Spades", "9"),
    ("Clubs", "9"),
    ("Diamonds", "9"),
    ("Hearts", "2"),
])

full_house = make_hand([
    ("Hearts", "4"),
    ("Spades", "4"),
    ("Clubs", "4"),
    ("Diamonds", "7"),
    ("Hearts", "7"),
])

flush = make_hand([
    ("Clubs", "2"),
    ("Clubs", "5"),
    ("Clubs", "8"),
    ("Clubs", "Jack"),
    ("Clubs", "King"),
])

straight = make_hand([
    ("Hearts", "3"),
    ("Spades", "4"),
    ("Clubs", "5"),
    ("Diamonds", "6"),
    ("Hearts", "7"),
])

three_kind = make_hand([
    ("Hearts", "8"),
    ("Spades", "8"),
    ("Clubs", "8"),
    ("Diamonds", "2"),
    ("Hearts", "5"),
])

two_pair = make_hand([
    ("Hearts", "3"),
    ("Spades", "3"),
    ("Clubs", "6"),
    ("Diamonds", "6"),
    ("Hearts", "King"),
])

one_pair = make_hand([
    ("Hearts", "10"),
    ("Spades", "10"),
    ("Clubs", "4"),
    ("Diamonds", "7"),
    ("Hearts", "Ace"),
])

high_card = make_hand([
    ("Hearts", "2"),
    ("Spades", "5"),
    ("Clubs", "8"),
    ("Diamonds", "Jack"),
    ("Hearts", "King"),
])

testutils.Test.assert_equals(
    solution.is_royal_flush(royal_flush),
    True,
    "is_royal_flush()"
)

testutils.Test.assert_equals(
    solution.is_straight_flush(straight_flush),
    True,
    "is_straight_flush()"
)

testutils.Test.assert_equals(
    solution.is_four_of_a_kind(four_kind),
    True,
    "is_four_of_a_kind()"
)

testutils.Test.assert_equals(
    solution.is_full_house(full_house),
    True,
    "is_full_house()"
)

testutils.Test.assert_equals(
    solution.is_flush(flush),
    True,
    "is_flush()"
)

testutils.Test.assert_equals(
    solution.is_straight(straight),
    True,
    "is_straight()"
)

testutils.Test.assert_equals(
    solution.is_three_of_a_kind(three_kind),
    True,
    "is_three_of_a_kind()"
)

testutils.Test.assert_equals(
    solution.is_two_pair(two_pair),
    True,
    "is_two_pair()"
)

testutils.Test.assert_equals(
    solution.is_one_pair(one_pair),
    True,
    "is_one_pair()"
)

testutils.Test.assert_equals(
    solution.get_best_hand(royal_flush),
    "Royal Flush",
    "get_best_hand() - Royal Flush"
)

testutils.Test.assert_equals(
    solution.get_best_hand(straight_flush),
    "Straight Flush",
    "get_best_hand() - Straight Flush"
)

testutils.Test.assert_equals(
    solution.get_best_hand(four_kind),
    "Four of a Kind",
    "get_best_hand() - Four of a Kind"
)

testutils.Test.assert_equals(
    solution.get_best_hand(full_house),
    "Full House",
    "get_best_hand() - Full House"
)

testutils.Test.assert_equals(
    solution.get_best_hand(flush),
    "Flush",
    "get_best_hand() - Flush"
)

testutils.Test.assert_equals(
    solution.get_best_hand(straight),
    "Straight",
    "get_best_hand() - Straight"
)

testutils.Test.assert_equals(
    solution.get_best_hand(three_kind),
    "Three of a Kind",
    "get_best_hand() - Three of a Kind"
)

testutils.Test.assert_equals(
    solution.get_best_hand(two_pair),
    "Two Pair",
    "get_best_hand() - Two Pair"
)

testutils.Test.assert_equals(
    solution.get_best_hand(one_pair),
    "One Pair",
    "get_best_hand() - One Pair"
)

testutils.Test.assert_equals(
    solution.get_best_hand(high_card),
    "High Card",
    "get_best_hand() - High Card"
)

print("\nFinished all tests.")
