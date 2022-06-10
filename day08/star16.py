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
program_fail = read_program('input_fail.txt')
program_pass = read_program('input_pass.txt')

def terminates(program):
	visited = set()
	line_num = 0
	accum = 0
	while True:
		visited.add(line_num)
		try:
			op, arg = program[line_num]
		except IndexError:
			if line_num < 0 or line_num > len(program):
				return False, accum
			return True, accum
		line_num, accum = do_operation(line_num, op, arg, accum)
		if line_num in visited:
			return False, accum

print("original program: terminates = {}, accum = {}".format(*terminates(program)))
print("fail test program: terminates = {}, accum = {}".format(*terminates(program_fail)))
print("pass test program: terminates = {}, accum = {}".format(*terminates(program_pass)))


line_num = 0
results = []
accum_set = set()
while True:
	try:
		op, arg = program[line_num]
	except IndexError:
		print("Ran out of lines!")
		break
	old_op = op
	if op == 'acc':
		line_num += 1
		continue
	elif op == 'nop':
		op = 'jmp'
	elif op == 'jmp':
		op = 'nop'
	program[line_num] = (op, arg)
	passed, accum = terminates(program)
	if passed:
		results.append((line_num, old_op, op, arg, accum))
		accum_set.add(accum)
	program[line_num] = (old_op, arg)
	line_num += 1

print("modified line {}, {}->{}, arg = {}, accum={}".format(*results[0]))