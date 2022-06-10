import numpy as np

class Boat:
	def __init__(self, pos=np.array([0, 0], dtype='int'), dir='E'):
		self.pos = pos
		self.dir = dir

		self.dir_dict = {'E': np.array([1, 0]),
		                 'S': np.array([0, -1]),
		                 'W': np.array([-1, 0]),
		                 'N': np.array([0, 1])}
		self.right_cycle = ['E', 'S', 'W', 'N']
		self.left_cycle = ['E', 'N', 'W', 'S']

	def update(self, cmd, arg):
		if cmd == 'F':
			cmd = self.dir
		elif cmd == 'L':
			self.rotate('L', arg)
			return
		elif cmd == 'R':
			self.rotate('R', arg)
			return
		self.pos += self.dir_dict[cmd]*arg

	def rotate(self, direction, amount):
		if direction == 'L':
			cycle = self.left_cycle
		else:
			cycle = self.right_cycle
		cur_index = cycle.index(self.dir)
		new_index = (cur_index + amount) % 4
		new_direction = cycle[new_index]
		self.dir = new_direction


def parse_instructions(input_file='input.txt'):
	instructions_list = []
	for line in open(input_file):
		instruction = line[0]
		number = int(line[1:])
		if instruction in ['L', 'R']:
			number = number // 90
		instructions_list.append((instruction, number))
	return instructions_list


instructions = parse_instructions()
# instructions = parse_instructions('input_test.txt')

boat = Boat()

for cmd, arg in instructions:
	boat.update(cmd, arg)

print("Manhattan distance = ", np.sum(np.abs(boat.pos)))
