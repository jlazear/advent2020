import numpy as np
from time import time

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

def make_array(max_line, pad=100):
    max_size = max_line*2 + 1 + 2*pad
    array = np.zeros([max_size, max_size], dtype='uint8')
    return array
    
def update_tile(array, instruction, idict, ref_ind):
    row_col = [0, 0]
    for direction in instruction:
        row_col += idict[direction]
    array[ref_ind + row_col[0], ref_ind + row_col[1]] = (array[ref_ind + row_col[0], ref_ind + row_col[1]] + 1) % 2
    return array

def make_pattern(fname, pad=100):
    instructions_list = parse_file(fname)
    maxlen = 2*max([len(instructions) for instructions in instructions_list])
    array = make_array(maxlen, pad)
    for instruction in instructions_list:
        array = update_tile(array, instruction, idict, maxlen+pad)
    return array

def update_pattern(pattern):
    to_update = {0: [], 1: []}

    adjacent = np.array([idict[d] for d in ('e', 'w', 'sw', 'se', 'nw', 'ne')])
    for i, j in np.ndindex(*np.shape(pattern)):
        if (i + j) % 2 == 1:
            continue
        if i < 1 or i > len(pattern) - 3 or j < 1 or j > len(pattern[0]) - 3:
            continue
        adjacent_values = []
        for k, l in adjacent:
            adjacent_values.append(pattern[i + k, j + l])
        s = sum(adjacent_values)
        if pattern[i, j] and (s == 0 or s > 2):
            to_update[0].append([i, j])
        elif not pattern[i, j] and s == 2:
            to_update[1].append([i, j])
    
    for i, j in to_update[0]:
        pattern[i, j] = 0
    for i, j in to_update[1]:
        pattern[i, j] = 1
    
    return pattern

def solve(fname, iterations=100):
    pattern = make_pattern(fname, pad=iterations)
    for i in range(iterations):
        print("Day {}: {}".format(i, np.sum(pattern)))  #DELME
        pattern= update_pattern(pattern)
    return np.sum(pattern)

t0 = time()
# print("Day 100: ", solve('input_test.txt'))
print("Day 100: ", solve('input.txt'))
print("elapsed time = ", time() - t0)