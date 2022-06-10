import numpy as np
from collections import Counter, defaultdict
from scipy.signal import convolve2d
from copy import copy
import time

def make_seamonster(fname):
    with open(fname) as f:
        s = f.read().replace('#', '1').replace(' ', '0')
    subblocks = s.split('\n')
    tile = [[c for c in subblock] for subblock in subblocks]
    tile = np.array(tile, dtype='uint8')
    return tile

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

    edges_dict = {}
    edges_dict['T'] = tuple(tile[0, :])
    edges_dict['B'] = tuple(tile[-1, :])
    edges_dict['L'] = tuple(tile[:, 0])
    edges_dict['R'] = tuple(tile[:, -1])
    edges_dict['rT'] = tuple(tile[0, ::-1])
    edges_dict['rB'] = tuple(tile[-1, ::-1])
    edges_dict['rL'] = tuple(tile[::-1, 0])
    edges_dict['rR'] = tuple(tile[::-1, -1])

    return edges, edges_dict

def check_match(question_tile, edges_set):
    num_matched_tiles = len(question_tile.intersection(edges_set))
    if num_matched_tiles == 4:
        return True, num_matched_tiles
    else:
        return False, num_matched_tiles

def rotate_tile(block_num, d, ed, match_locs):
    """rotates in positive direction (counterclockwise)"""
    tile = d[block_num]
    tile = np.rot90(tile)
    d[block_num] = tile

    _, edges_dict = get_edges(tile)
    ed[block_num] = edges_dict
    
    transform_dict = {'T': 'L',
                      'L': 'B',
                      'B': 'R',
                      'R': 'T',
                      'rT': 'rL',
                      'rL': 'rB',
                      'rB': 'rR',
                      'rR': 'rT'}
    match_locs[block_num] = [transform_dict[x] for x in match_locs[block_num]]
    return block_num, d, ed, match_locs
    
def fliplr_tile(block_num, d, ed, match_locs):
    """flips left-to-right, across a vertical axis"""
    tile = d[block_num]
    tile = np.fliplr(tile)
    d[block_num] = tile

    _, edges_dict = get_edges(tile)
    ed[block_num] = edges_dict
    
    transform_dict = {'T': 'rT',
                      'L': 'rR',
                      'B': 'rB',
                      'R': 'rL',
                      'rT': 'T',
                      'rL': 'R',
                      'rB': 'B',
                      'rR': 'L'}
    match_locs[block_num] = [transform_dict[x] for x in match_locs[block_num]]
    return block_num, d, ed, match_locs

def do_nothing(block_num, d, ed, match_locs):
    return block_num, d, ed, match_locs

def find_match(edge, match_id_list, ed):
    for match_id in match_id_list:
        edges_dict = ed[match_id]
        for loc, edge2 in edges_dict.items():
            if edge2 == edge:
                return match_id, loc
    raise Exception("Didn't find a match, when it should've...")

def make_image_from_image_ids(image_ids, d):
    image = np.zeros((12*8, 12*8), dtype='uint8')
    for i, j in np.ndindex(*image_ids.shape):
        image_id = image_ids[i, j]
        tile = d[image_id]
        image[i*8:(i+1)*8, j*8:(j+1)*8] = tile[1:9, 1:9]
    return image

t0 = time.time()

with open('input.txt') as f:
    s = f.read().replace('#', '1').replace('.', '0')

blocks = s.split('\n\n')
d = {}   # block_num: tile array
e = {}   # block_num: edges set 
ed = {}  # block_num: edges_dict
all_edges = set()
for block in blocks:
    if not block:
        continue
    block_num, tile = parse_block(block)
    d[block_num] = tile
    edges, edges_dict = get_edges(tile)
    e[block_num] = edges
    ed[block_num] = edges_dict

# this is a horrifying N^2 algorithm, but N is small here...
match_ids = defaultdict(list)
match_locs = defaultdict(list)
for block_num, edges in e.items():
    for block_num2, edges2 in e.items():
        if block_num2 == block_num:
            continue
        intersection = edges.intersection(edges2)
        num_match = len(intersection)
        if num_match:
            match_ids[block_num].append(block_num2)
            edges_dict = ed[block_num]
            for loc, edge in edges_dict.items():
                if edge in intersection:
                    match_locs[block_num].append(loc)

# we'll arbitrarily set tile 1093 to be the TOP LEFT corner
image_ids = np.zeros((12, 12), dtype='uint16')
rotate_tile(1093, d, ed, match_locs)
image_ids[0, 0] = 1093
# match up the first column
transformB = {'R': rotate_tile,
             'B': lambda block_num, d, ed, match_locs: rotate_tile(*rotate_tile(*fliplr_tile(block_num, d, ed, match_locs))),
             'L': lambda block_num, d, ed, match_locs: rotate_tile(*fliplr_tile(block_num, d, ed, match_locs)),
             'T': do_nothing,
             'rR': lambda block_num, d, ed, match_locs: fliplr_tile(*rotate_tile(block_num, d, ed, match_locs)),
             'rB': lambda block_num, d, ed, match_locs: rotate_tile(*rotate_tile(block_num, d, ed, match_locs)),
             'rL': lambda block_num, d, ed, match_locs: rotate_tile(*rotate_tile(*rotate_tile(block_num, d, ed, match_locs))),
             'rT': lambda block_num, d, ed, match_locs: fliplr_tile(block_num, d, ed, match_locs),
             }

transformR = {'rT': rotate_tile,
             'rL': lambda block_num, d, ed, match_locs: rotate_tile(*rotate_tile(*fliplr_tile(block_num, d, ed, match_locs))),
             'T': lambda block_num, d, ed, match_locs: rotate_tile(*fliplr_tile(block_num, d, ed, match_locs)),
             'L': do_nothing,
             'rB': lambda block_num, d, ed, match_locs: fliplr_tile(*rotate_tile(block_num, d, ed, match_locs)),
             'rR': lambda block_num, d, ed, match_locs: rotate_tile(*rotate_tile(block_num, d, ed, match_locs)),
             'B': lambda block_num, d, ed, match_locs: rotate_tile(*rotate_tile(*rotate_tile(block_num, d, ed, match_locs))),
             'R': lambda block_num, d, ed, match_locs: fliplr_tile(block_num, d, ed, match_locs),
             }

for i in range(len(image_ids) - 1):
    image_id = image_ids[i, 0]
    bottom = ed[image_id]['B']
    match_id_list = match_ids[image_id]
    match_id, loc = find_match(bottom, match_id_list, ed)
    image_ids[i+1, 0] = match_id
    transformB[loc](match_id, d, ed, match_locs)
print('-'*10)
for i in range(len(image_ids)):
    for j in range(len(image_ids) - 1):
        image_id = image_ids[i, j]
        right = ed[image_id]['R']
        match_id_list = match_ids[image_id]
        match_id, loc = find_match(right, match_id_list, ed)
        image_ids[i, j+1] = match_id
        transformR[loc](match_id, d, ed, match_locs)

image = make_image_from_image_ids(image_ids, d)

def check_seamonster(sea_monster, image, image_copy, sm_rows, sm_cols):
    for _ in range(4):
        sea_monster = np.rot90(sea_monster)  # calls rotation an extra time oh well
        sm_h, sm_w = np.shape(sea_monster)
        sm_filt = convolve2d(image, sea_monster, mode='same')
        sm_locs = np.where(sm_filt==num_pound)
        sm_rows.extend(sm_locs[0])
        sm_cols.extend(sm_locs[1])
        for row, col in zip(sm_locs[0], sm_locs[1]):
            image_copy[int(np.floor(row-sm_h/2)):int(np.ceil(row+(sm_h-1)/2)), int(np.floor(col-sm_w/2)):int(np.ceil(col+(sm_w-1)/2))] = sea_monster*2
    return sm_rows, sm_cols, image_copy

sea_monster = make_seamonster('sea_monster.txt')
num_pound = np.sum(np.array(sea_monster))
nrow, ncol = np.shape(image)
sea_monster_counter = copy(image)
sm_rows = []
sm_cols = []
sm_rows, sm_cols, sea_monster_counter = check_seamonster(sea_monster, image, sea_monster_counter, sm_rows, sm_cols)
sea_monster = np.fliplr(sea_monster)
sm_rows, sm_cols, sea_monster_counter = check_seamonster(sea_monster, image, sea_monster_counter, sm_rows, sm_cols)
print('RESULT MAYBE', np.sum(image) - np.shape(np.where(sea_monster_counter==2))[1])
print("execution time = ", time.time() - t0)