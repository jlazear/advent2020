import numpy as np
from collections import Counter
import time

def parse_block(block):
    subblocks = block.split('\n')
    block_num = int(subblocks[0].split()[1].strip(':'))
    tile = [[c for c in subblock] for subblock in subblocks[1:]]
    tile = np.array(tile, dtype='uint8')
    return block_num, tile

def get_edges(tile):
    edges = set()
    edges.add(tuple(tile[0, :]))
    edges.add(tuple(tile[-1, :]))
    edges.add(tuple(tile[:, 0]))
    edges.add(tuple(tile[:, -1]))
    edges.add(tuple(tile[0, ::-1]))
    edges.add(tuple(tile[-1, ::-1]))
    edges.add(tuple(tile[::-1, 0]))
    edges.add(tuple(tile[::-1, -1]))
    return edges

def check_match(question_tile, edges_set):
    num_matched_tiles = len(question_tile.intersection(edges_set))
    if num_matched_tiles == 4:
        return True, num_matched_tiles
    else:
        return False, num_matched_tiles

t0 =  time.time()

with open('input.txt') as f:
    s = f.read().replace('#', '1').replace('.', '0')

blocks = s.split('\n\n')
d = {}
e = {}
all_edges = set()
for block in blocks:
    if not block:
        continue
    block_num, tile = parse_block(block)
    d[block_num] = tile
    edges = get_edges(tile)
    all_edges.update(edges)
    e[block_num] = edges

# this is a horrifying N^2 algorithm, but N is small here...
num_matches = Counter()
for block_num, edges in e.items():
    for block_num2, edges2 in e.items():
        if block_num2 == block_num:
            continue
        num_match = len(edges.intersection(edges2))
        num_matches[block_num] += num_match

print(np.prod([key for key, value in num_matches.items() if value == 4], dtype='int64'))
print("execution time = ", time.time() - t0)