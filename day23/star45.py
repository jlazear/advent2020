puzzle_input = 716892543
puzzle_input_test = 389125467

def rotate(x, n):
    return x[n:] + x[:n]

def play(cups, current, num_pickup=3, verbose=False):
    if current:
        cups = rotate(cups, current)
        current = 0
    min_cups, max_cups = min(cups), max(cups)
    select = cups[current+1:current+num_pickup+1]
    remain = cups[:current+1] + cups[current+num_pickup+1:]
    destination = cups[current] - 1
    if destination < min_cups:
        destination = max_cups
    while destination not in remain:
        destination -= 1
        if destination < min_cups:
            destination = max_cups
    destination_index = remain.index(destination)
    new_cups = remain[:destination_index+1] + select + remain[destination_index+1:]
    new_current = new_cups.index(cups[current])
    new_current = (new_current + 1) % len(cups)
    if verbose:
        # print("current = ", current)  #DELME
        print("current value = ", cups[current])  #DELME
        print("pick up: ", select)  #DELME
        # print("remain = ", remain)  #DELME
        print("destination = ", destination)  #DELME
        # print("destination_index = ", destination_index)  #DELME
        # print("new cups = ", new_cups)  #DELME
        # print("new current = ", new_current)  #DELME
    return new_cups, new_current

def play_repeatedly(puzzle_input, iterations=100, current=0, verbose=False):
    i = 1
    cups = [int(x) for x in str(puzzle_input)]
    for _ in range(iterations):
        if verbose: print("-- move {} --\ncups: {}".format(i, cups))  #DELME
        i += 1
        cups, current = play(cups, current, verbose=verbose)
        if verbose: print('-'*10)  #DELME
    return cups, current


cups, current = play_repeatedly(puzzle_input_test, 10, verbose=True)
print("test final = ", cups)

cups, current = play_repeatedly(puzzle_input, 100)
oneindex = cups.index(1)
cups = rotate(cups, oneindex)
print("final = ", cups)
print(''.join([str(x) for x in cups[1:]]))