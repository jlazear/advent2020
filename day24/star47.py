import numpy as np

def parse_line(line):
    instructions = []
    store = ''
    for c in line:
        if store:
            instructions.append(store + c)
            store = ''
        elif c in ('s', 'n'):
            store = c
        else:
            instructions.append(c)
    return instructions
        
def parse_file(fname):
    return [parse_line(line.strip()) for line in open(fname)]

idict = {'e': np.array([0, 2]),
         'w': np.array([0, -2]),
         'sw': np.array([-1, -1]),
         'se': np.array([-1, 1]),
         'nw': np.array([1, -1]),
         'ne': np.array([1, 1])}

def make_array(max_line):
    max_size = max_line*2 + 1
    array = np.zeros([max_size, max_size], dtype='uint8')
    return array
    
def update_tile(array, instruction, idict, ref_ind):
    row_col = [0, 0]
    for direction in instruction:
        row_col += idict[direction]
    array[ref_ind + row_col[0], ref_ind + row_col[1]] = (array[ref_ind + row_col[0], ref_ind + row_col[1]] + 1) % 2
    return array

def solve(fname):
    instructions_list = parse_file(fname)
    maxlen = 2*max([len(instructions) for instructions in instructions_list])
    array = make_array(maxlen)
    for instruction in instructions_list:
        array = update_tile(array, instruction, idict, maxlen)
    return np.sum(array)

print("TEST RESULTS = ", solve('input_test.txt'))
print("REAL RESULTS = ", solve('input.txt'))
