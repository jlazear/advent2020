from collections import deque
from copy import copy

def apply_mask(memloc, mask):
    bmemloc = "{:036b}".format(memloc)
    blist = [c for c in bmemloc]
    for i in range(len(blist)):
        m = mask[i]
        b = blist[i]
        if m == '1':
            blist[i] = '1'
        elif m == '2':
            blist[i] = '0'
    return int('0b' + ''.join(blist), 2)

def generate_masks(mask):
    q = deque([[c for c in mask],])
    found_X = True
    while q and found_X:
        item = q.popleft()
        found_X = False
        for i, c in enumerate(item):
            if c == 'X':
                found_X = True
                item1 = copy(item)
                item1[i] = '2'
                item2 = copy(item)
                item2[i] = '1'
                q.append(item1)
                q.append(item2)
                break
        if found_X is False:
            q.appendleft(item)
    return [''.join(item) for item in q]


commands = [line.strip() for line in open('input.txt')]
d = {}
masks = []
for command in commands:
    words = command.split('=')
    if words[0].strip() == 'mask':
        masks = generate_masks(words[1].strip())
    else:
        memloc = int(words[0].split('[')[1].strip(' ]'))
        value = int(words[1])
        memlocs = [apply_mask(memloc, mask) for mask in masks]
        for ml in memlocs:
            d[ml] = value

print(sum(d.values()))