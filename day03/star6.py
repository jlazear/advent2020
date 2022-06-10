with open('input.txt') as f:
	tree_map = [line.strip() for line in f.readlines()]

def check_slope(tree_map, delta_x, delta_y):
	ypos = 0
	xpos = 0

	ymax = len(tree_map)
	xmax = len(tree_map[0])

	tree_count = 0
	while ypos < ymax:
		if tree_map[ypos][xpos] == '#':
			tree_count += 1
		ypos += delta_y
		xpos = (xpos + delta_x) % xmax
	return tree_count

slopes = [(1, 1),
          (3, 1),
          (5, 1),
          (7, 1),
          (1, 2)]

trees_encountered = [check_slope(tree_map, *slope) for slope in slopes]
product = 1
for item in trees_encountered:
	product *= item

print("total number of trees encountered = ", product)