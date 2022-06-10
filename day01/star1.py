TARGET = 2020

seen = set()

for line in open('input.txt'):
	num = int(line)
	if TARGET - num in seen:
		print(num*(TARGET-num))
	else:
		seen.add(num)
