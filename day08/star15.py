def parse_line(line):
	op, arg = line.split()
	arg = int(arg)
	return op, arg

def read_program(fname):
	program = []
	for line in open(fname):
		if line:
			op, arg = parse_line(line)
			program.append((op, arg))
	return program

def do_operation(cur_line, op, arg, accum):
	if op == 'nop':
		return cur_line + 1, accum
	elif op == 'jmp':
		return cur_line + arg, accum
	elif op == 'acc':
		return cur_line + 1, accum + arg

program = read_program('input.txt')

visited = set()
line_num = 0
accum = 0
while True:
	visited.add(line_num)
	op, arg = program[line_num]
	line_num, accum = do_operation(line_num, op, arg, accum)
	if line_num in visited:
		break

print("accumulator value = ", accum)