import random, os, sys

card_name = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
             10: '10', 11: 'Jack', 12: 'Queen', 13: 'King'}
card_suit = {'c': 'Clubs', 'h': 'Hearts', 's': 'Spades', 'd': 'Diamonds'}


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return (card_name[self.rank] + " Of " + card_suit[self.suit])

    def getRank(self):
        return (self.rank)

    def getSuit(self):
        return (self.suit)

    def value(self):
        if self.rank > 9:
            return (10)
        else:
            return (self.rank)


def show_hand(hand):
    for card in hand:
        print(card)


def hand_count(hand):
    hand_count = 0
    for card in hand:
        hand_count += card.value()
    return (hand_count)


def gameEnd(score):
    print("YOUR POINTS: " + str(hand_count(hand['player'])))
    print("DEALER'S POINTS: " + str(hand_count(hand['dealer'])))
    print()
    print("Yay! The dealer busted. You win!")


deck = []
suits = ['c', 'h', 'd', 's']
score = {'dealer': 0, 'player': 0}
hand = {'dealer': [], 'player': []}

for suit in suits:
    for rank in range(1, 14):
        deck.append(Card(rank, suit))

keepPlaying = True

print("Blackjack\n")

while keepPlaying:
    # shuffling
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)

    hand['player'].append(deck.pop(0))
    hand['dealer'].append(deck.pop(0))
    hand['player'].append(deck.pop(0))
    hand['dealer'].append(deck.pop(0))

    playPlayer = True
    bustedPlayer = False

    print("\nDEALER'S SHOW CARD:")
    print(str(hand['dealer'][-1]))
    print()

    while playPlayer:
        os.system('clear')

        print("\nYOUR CARDS: ")
        show_hand(hand['player'])
        print()

        inputCycle = True

        while inputCycle:
            user_input = input("Hit or stand? (hit/stand): ")
            if user_input == 'hit' or 'stand':
                inputCycle = False
        if user_input == 'hit':
            hand['player'].append(deck.pop(0))
            if hand_count(hand['player']) > 21:
                playPlayer = False
                bustedPlayer = True
        elif user_input == 'stand':
            playPlayer = False
        else:
            print("ERROR - Invalid")
            quit()

    playDealer = True
    bustedDealer = False

    while not bustedPlayer and playDealer:

        if hand_count(hand['dealer']) < 17:
            hand['dealer'].append(deck.pop(0))
        else:
            print("\nYou Lost")
            print("YOUR POINTS: " + str(hand_count(hand['player'])))
            print("DEALER'S POINTS: " + str(hand_count(hand['dealer'])))
            playDealer = False
        if hand_count(hand['dealer']) > 21:
            playDealer = False
            bustedDealer = True

    if bustedPlayer:
        score['dealer'] += 1
        gameEnd(score)
    elif bustedDealer:
        score['player'] += 1
    elif hand_count(hand['player']) > hand_count(hand['dealer']):
        score['player'] += 1
    else:
        score['dealer'] += 1

    quit_option = input("\nPlay again? (y/n): ")

    if quit_option == "y":
        deck.extend(hand['dealer'])
        deck.extend(hand['player'])

    else:
        print("Come back soon!")
        quit()

    del hand['dealer'][:]
    del hand['player'][:]
