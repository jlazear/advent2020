from copy import deepcopy

def load_grid(fname='input.txt'):
	grid = [[c for c in line.strip()] for line in open(fname)]
	return grid

def find_nearest_seats(row, col, grid):
	numrows = len(grid)
	numcols = len(grid[0])
	cur_state = grid[row][col]
	nearest_seats = []
	if cur_state == '.': 
		return nearest_seats

	# up
	drow = 1
	while row - drow >= 0:
		if grid[row - drow][col] == 'L':
			nearest_seats.append((row - drow, col))
			break
		drow += 1

	# up right
	drow = 1
	dcol = 1
	while row - drow >= 0 and col + dcol < numcols:
		if grid[row - drow][col + dcol] == 'L':
			nearest_seats.append((row - drow, col + dcol))
			break
		drow += 1
		dcol += 1

	# right
	dcol = 1
	while col + dcol < numcols:
		if grid[row][col + dcol] == 'L':
			nearest_seats.append((row, col + dcol))
			break
		dcol += 1

	# down right
	drow = 1
	dcol = 1
	while row + drow < numrows and col + dcol < numcols:
		if grid[row + drow][col + dcol] == 'L':
			nearest_seats.append((row + drow, col + dcol))
			break
		drow += 1
		dcol += 1

	# down
	drow = 1
	while row + drow < numrows:
		if grid[row + drow][col] == 'L':
			nearest_seats.append((row + drow, col))
			break
		drow += 1

	# down left
	drow = 1
	dcol = 1
	while row + drow < numrows and col - dcol >= 0:
		if grid[row + drow][col - dcol] == 'L':
			nearest_seats.append((row + drow, col - dcol))
			break
		drow += 1
		dcol += 1

	# left
	dcol = 1
	while col - dcol >= 0:
		if grid[row][col - dcol] == 'L':
			nearest_seats.append((row, col - dcol))
			break
		dcol += 1

	# up left
	drow = 1
	dcol = 1
	while row - drow >= 0 and col - dcol >= 0:
		if grid[row - drow][col - dcol] == 'L':
			nearest_seats.append((row - drow, col - dcol))
			break
		drow += 1
		dcol += 1

	return nearest_seats

def nearest_seats_map(grid):
	m = {}
	for row, items in enumerate(grid):
		for col, item in enumerate(items):
			nearest_seats = find_nearest_seats(row, col, grid)
			if nearest_seats:
				m[(row, col)] = nearest_seats
	return m

def transition(row, col,grid, m):
	cur_state = grid[row][col]
	if cur_state == '.':
		return cur_state
	nearest_seats = m[(row, col)]
	count = 0
	for mrow, mcol in nearest_seats:
		if grid[mrow][mcol] == '#':
			count += 1
	if cur_state == 'L' and count == 0:
		return '#'
	elif cur_state == '#' and count >= 5:
		return 'L'
	else:
		return cur_state

def update(grid, temp_grid, m):
	for row, items in enumerate(grid):
		for col, item in enumerate(items):
			temp_grid[row][col] = transition(row, col, grid, m)
	return temp_grid, grid

def count_people(grid, char='#'):
	return sum([sum([1 for item in row if item == char]) for row in grid])

def pretty_print(grid):
	return '\n'.join([''.join(row) for row in grid])

# grid = load_grid('input_map1_test.txt')
# grid = load_grid('input_test.txt')
grid = load_grid()
m = nearest_seats_map(grid)

temp_grid = deepcopy(grid)
prev_num_people = count_people(grid)
num_people = -1

i = 0
while num_people != prev_num_people:
	if i % 1 == 0:
		print("i = ", i) 
	i += 1
	prev_num_people = num_people
	grid, temp_grid = update(grid, temp_grid, m)
	num_people = count_people(grid)

print("num people = ", num_people)
