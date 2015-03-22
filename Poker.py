__author__ = 'samarthshah'
import random


def poker(hands):
    max_hand = max(hands, key=hand_rank)
    return [hand for hand in hands if hand_rank(hand) == hand_rank(max_hand)]


def hand_rank(hand):
    "Return a value indicating how high the hand ranks."
    # counts is the count of each rank
    # ranks lists corresponding ranks
    # [6C, 7C, 8C, 9C, TC] ==> [10, 9,8,7,6]
    # E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    ranks = ranks if ranks != [14, 5, 4, 3, 2] else [5, 4, 3, 2, 1]
    isFlush = flush(hand)
    isStraight = straight(ranks)

    if isFlush and isStraight:                           # straight flush
        return (8, max(ranks))

    elif kind(4, ranks):                                # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))

    elif kind(3, ranks) and kind(2, ranks):           # full house
        return (6, kind(3, ranks), kind(2, ranks))

    elif isFlush:                                       # Flush
        return (5, ranks)

    elif isStraight:                                    # straight
        return (4, max(ranks))

    elif kind(3, ranks):                                # 3 of a kind
        return (3, kind(3, ranks), ranks)

    elif two_pair(ranks):                               # pair of two
        return (2, two_pair(ranks), ranks)

    elif kind(2, ranks):                                # kind
        return (1, kind(2, ranks), ranks)

    else:                                               # high card
        return (0, ranks)


def card_ranks(hand):
    rank_string = '--23456789TJQKA'
    ranks = [rank_string.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks


def straight(ranks):
    first_element = ranks[0]
    expected_last_element = first_element - 5
    return ranks == range(first_element, expected_last_element, -1)


def flush(hand):
    suit_list = [s for r, s in hand]
    return suit_list.count(suit_list[0]) == 5


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in set(ranks):
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    # 10, 10, 9, 9, 2
    result = [r for r in set(ranks) if ranks.count(r) == 2]
    result.sort(reverse=True)
    return tuple(result) if len(result) == 2 else None

my_deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']


def deal(players, card_per_hand=5, deck = my_deck):
    random.shuffle(deck)
    list_of_decks = [deck[card_per_hand * i:card_per_hand * (i+1)] for i in range(players)]
    print 'Number of players: ', players
    print 'The decks generated for this game are:'
    for x in range(len(list_of_decks)):
        print 'Player {}  ---> {}'.format(x+1 , list_of_decks[x])
    return list_of_decks


if __name__ == '__main__':
    # print test()
    print 'Dealer is shuffling the cards randomly....'
    print 'Please wait...'
    list_of_decks = deal(10)
    print ''
    print 'And the winner(s) are: ', poker(list_of_decks)