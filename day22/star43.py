from collections import deque

with open('input.txt') as f:
    p1_str, p2_str = f.read().split('\n\n')

deck1 = deque([int(x) for x in p1_str.split('\n')[1:] if x])
deck2 = deque([int(x) for x in p2_str.split('\n')[1:] if x])

while deck1 and deck2:
    card1 = deck1.popleft()
    card2 = deck2.popleft()
    if card1 > card2:
        deck1.append(card1)
        deck1.append(card2)
    else:
        deck2.append(card2)
        deck2.append(card1)

print(sum([(len(deck1) - i)*card for i, card in enumerate(deck1)]))
print(sum([(len(deck1) - i)*card for i, card in enumerate(deck2)]))