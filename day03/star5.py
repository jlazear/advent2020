DELTA_X = 3
DELTA_Y = 1

with open('input.txt') as f:
	tree_map = [line.strip() for line in f.readlines()]

ypos = 0
xpos = 0

ymax = len(tree_map)
xmax = len(tree_map[0])

tree_count = 0
while ypos < ymax:
	if tree_map[ypos][xpos] == '#':
		tree_count += 1
	ypos += DELTA_Y
	xpos = (xpos + DELTA_X) % xmax

print("number of trees encountered = ", tree_count)