# Deal cards

# Otption for player to hit/split/double/insurance/stand

# action happening according to player input

# end result

# Repeat
import requests
from pprint import pprint


def dealCards(deck_id):

    hands = {"player": {}, "dealer": [],}
    requests.get("http://deckofcardsapi.com/api/deck/" + deck_id + "/shuffle/")
    r = requests.get("http://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=2")
    hands['player']['hand1'] = r.json()['cards']
    r = requests.get("http://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=2")
    hands['dealer'] = r.json()['cards']
    return hands



def hit(hands, deck_id):
    r = requests.get("http://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=1")
    hands['player']['hand1'] += r.json()['cards']
    return hands


def getvalue(hand):
    sum = 0
    aceCount = 0
    for card in hand:
        if card['value'] == 'JACK' or card['value'] == 'QUEEN' or card['value'] == 'KING':
            sum += 10
        elif card['value'].isnumeric():
            sum += int(card['value'])
        else:
            aceCount += 1
            sum += 11
    while aceCount > 0:
        if sum > 21:
            aceCount = aceCount - 1
            sum = sum - 10
        else:
            break
    return sum


def split(currentHand, player):
    player['hand' + str(1 + len(player))] = currentHand.pop(1)
    return player



def main():
    r = requests.get("http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    deck = r.json()['deck_id']

    hands = dealCards(deck)
    print(split(hands['player']['hand1'], hands['player']))
    # hands = split(hands['player'])
    
    # pprint(hands['player']['hand1'])
    # print(getvalue(hands['player']['hand1']))

    
if __name__ == '__main__':
    main()