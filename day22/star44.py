from copy import copy
from time import time

t0 = time()

fname = 'input_test.txt'
with open(fname) as f:
    p1_str, p2_str = f.read().split('\n\n')

deck1 = [int(x) for x in p1_str.split('\n')[1:] if x]
deck2 = [int(x) for x in p2_str.split('\n')[1:] if x]

i = 1
def play(deck1, deck2, verbosity=0):
    global i  #DELME
    if verbosity:
        print("="*10)  #DELME
        print("Game {}".format(i))  #DELME
        print("-"*10)
    i += 1  #DELME
    seen = set()
    seen_flag = False
    round_num = 1  #DELME
    while deck1 and deck2:
        if verbosity > 1:
            if round_num > 1: print('-'*5)  #DELME
            print("Round {}".format(round_num))  #DELME
            round_num += 1  #DELME
            print("deck1 = ", deck1)  #DELME
            print("deck2 = ", deck2)  #DELME
        seen_flag = (tuple([tuple(deck1), tuple(deck2)]) in seen)
        seen.add(tuple([tuple(deck1), tuple(deck2)]))
        if seen_flag:
            if verbosity > 1: print("Seen configuration before... terminating w/ winner = 1")  #DELME
            return 1, deck1, deck2
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if verbosity > 1:
            print("card1 = ", card1)  #DELME
            print("card2 = ", card2)  #DELME
        if len(deck1) >= card1 and len(deck2) >= card2:
            if verbosity > 1: print("Playing sub-game...")  #DELME
            deck1copy = copy(deck1[:card1])
            deck2copy = copy(deck2[:card2])
            winner, _, _ = play(deck1copy, deck2copy, verbosity)
        else:
            winner = 1 if card1 > card2 else 2
            if verbosity > 1: print("standard round, winner = ", winner)  #DELME
        if winner == 1:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    winner = 1 if deck1 else 2
    return winner, deck1, deck2

print(play(deck1, deck2, verbosity=2))

print(sum([(len(deck1) - i)*card for i, card in enumerate(deck1)]))
print(sum([(len(deck2) - i)*card for i, card in enumerate(deck2)]))
print("time elapsed = ", time() - t0)