from time import time

class Node:
    def __init__(self, value, cw=None, ccw = None):
        self.value = value
        self.cw = cw
        self.ccw = ccw

    def __str__(self):
        fmtstr = "Node(ccw={ccw}, {value}, cw={cw})"
        cw = self.cw.value if self.cw else None
        ccw = self.ccw.value if self.ccw else None
        return fmtstr.format(value=self.value, cw=cw, ccw=ccw)

    def __repr__(self):
        return self.__str__()
    
def make_linked_list(puzzle_input, pad_to=1000000):
    cups = [int(x) for x in str(puzzle_input)]
    current_node = Node(cups[0])
    low_cups = [current_node]
    node_dict = {current_node.value: current_node}
    for cup in cups[1:]:
        node = Node(cup, ccw=current_node)
        current_node.cw = node
        low_cups.append(node)
        node_dict[node.value] = node
        current_node = node

    if pad_to:
        max_cup = max(cups)
        for value in range(max_cup+1, pad_to+1):
            node = Node(value, ccw=current_node)
            current_node.cw = node
            current_node = node
            node_dict[node.value] = node
        first = low_cups[0]
    first = low_cups[0]
    current_node.cw = first
    first.ccw = current_node

    return low_cups, node_dict

def play(current, node_dict, lowest=1, highest=1000000):
    select_first = current.cw
    select_last = current.cw.cw.cw
    select_values = [current.cw.value, current.cw.cw.value, current.cw.cw.cw.value]

    # chop out the selected
    current.cw = select_last.cw
    select_last.cw.ccw = current

    # find the destination node
    destination = find_destination(current, select_values, node_dict, lowest=lowest, highest=highest)
    
    # insert selected between destination and destination.cw
    destination_cw = destination.cw
    destination.cw = select_first
    select_first.ccw = destination
    destination_cw.ccw = select_last
    select_last.cw = destination_cw

    # select new current cup
    current = current.cw
    return current
    
def find_destination(current, select_values, node_dict, lowest=1, highest=1000000):
    target_value = current.value - 1
    if target_value < lowest:
        target_value = highest
    while target_value in select_values:
        target_value -= 1
        if target_value < lowest:
            target_value = highest

    destination = node_dict[target_value]
    
    return destination    

def read_linked_list(current):
    first = current
    values = [str(first.value)]
    current = current.cw
    while current is not first:
        values.append(str(current.value))
        current = current.cw
    return ', '.join(values)

def play_repeatedly(current, node_dict, iterations=10000000, lowest=1, highest=1000000,
                    verbosity=100000):
    for i in range(iterations):
        if i % verbosity == 0:
            print("i = {} ({}/{})".format(i, i//verbosity, iterations//verbosity))
        current = play(current, node_dict, lowest=lowest, highest=highest)
    return current

def solve(puzzle_input, pad_to=1000000, iterations=10000000, verbosity=100000, timeit=True):
    t0 = time()
    lowest = min([int(x) for x in str(puzzle_input)])
    if pad_to is None:
        highest = max([int(x) for x in str(puzzle_input)])
    else:
        highest = pad_to
    low_nodes, node_dict = make_linked_list(puzzle_input, pad_to=pad_to)
    current = low_nodes[0]
    current = play_repeatedly(current, node_dict, iterations=iterations, lowest=lowest, highest=highest,
                              verbosity=verbosity)
    n1 = node_dict[1]
    if timeit:
        print("elapsed time = ", time() - t0)
    return n1.cw.value * n1.cw.cw.value

# puzzle_input_test = 389125467
# print(solve(puzzle_input_test))

puzzle_input = 716892543
print(solve(puzzle_input))