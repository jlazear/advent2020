TARGET = 2020

seen = set()
seen2 = {}

for line in open('input.txt'):
	num = int(line)
	if TARGET - num in seen2:
		num2, num3 = seen2[TARGET-num]
		print("nums are {}, {}, {}".format(num, num2, num3))
		print("product is {}".format(num*num2*num3))
	else:
		for num2 in seen:
			seen2[num + num2] = (num, num2)
		seen.add(num)
