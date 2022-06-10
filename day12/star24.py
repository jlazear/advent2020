import numpy as np

class Boat:
	def __init__(self, pos=np.array([0, 0], dtype='int'), dir='E'):
		self.pos = pos
		self.dir = dir
		self.waypoint = np.array([10, 1], dtype='int')

		self.dir_dict = {'E': np.array([1, 0], dtype='int'),
		                 'S': np.array([0, -1], dtype='int'),
		                 'W': np.array([-1, 0], dtype='int'),
		                 'N': np.array([0, 1], dtype='int')}

	def update(self, cmd, arg):
		if cmd == 'F':
			self.pos += self.waypoint*arg
			return
		elif cmd == 'L':
			self.rotate('L', arg)
			return
		elif cmd == 'R':
			self.rotate('R', arg)
			return
		self.waypoint += self.dir_dict[cmd]*arg

	def rotate(self, direction, amount):
		theta = (1 if direction == 'L' else -1) * np.pi/2 * amount
		rotmat = np.array([[np.cos(theta), -np.sin(theta)],
			               [np.sin(theta), np.cos(theta)]], dtype='int')
		self.waypoint = rotmat @ self.waypoint

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

