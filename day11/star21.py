from copy import deepcopy

grid = [[c for c in line.strip()] for line in open('input.txt')]

def transition(row, col, grid):
	numrows = len(grid)
	numcols = len(grid[0])
	count = 0
	cur_state = grid[row][col]
	if cur_state == '.': return '.'
	if row-1 >= 0:
		if col-1 >= 0 and grid[row-1][col-1] == '#': count += 1
		if grid[row-1][col] == '#': count += 1
		if col+1 < numcols and grid[row-1][col+1] == '#': count += 1
	if row+1 < numrows:
		if col-1 >= 0 and grid[row+1][col-1] == '#': count += 1
		if grid[row+1][col] == '#': count += 1
		if col+1 < numcols and grid[row+1][col+1] == '#': count += 1
	if col-1 >= 0 and grid[row][col-1] == '#': count += 1
	if col+1 < numcols and grid[row][col+1] == '#': count += 1
	next_state = cur_state
	if cur_state == 'L' and count == 0:
		next_state = '#'
	elif cur_state == '#' and count >= 4:
		next_state = 'L'
	return next_state

def count_people(grid, char='#'):
	return sum([sum([1 for item in row if item == char]) for row in grid])

def update(grid, temp_grid):
	for row, items in enumerate(grid):
		for col, item in enumerate(items):
			temp_grid[row][col] = transition(row, col, grid)
	return temp_grid, grid


temp_grid = deepcopy(grid)
prev_num_people = count_people(grid)
num_people = -1

while num_people != prev_num_people:
	prev_num_people = num_people
	grid, temp_grid = update(grid, temp_grid)
	num_people = count_people(grid)

print("num people = ", num_people)






# row-1, col-1   row-1, col    row-1, col+1
# row, col-1     row, col      row, col+1
# row+1, col-1   row+1, col,   row+1, col+1