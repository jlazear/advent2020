from collections import OrderedDict
nums = []
all_nums = []

i = 0
for line in open('input.txt'):
	num = int(line)
	
	if i <= 24:
		nums.append(num)
		all_nums.append(num)
		i += 1
		continue

	valid = False
	for a in nums:
		if num - a in nums:
			valid = True
			break
	if not valid:
		print("first invalid number: {}".format(num))
		break
	else:
		nums.pop(0)
		nums.append(num)
		all_nums.append(num)

for i in range(len(all_nums)):
	print("i = ", i)  #DELME
	a = all_nums[i]
	s = a
	j = i + 1
	while s < num and j < len(all_nums):
		s += all_nums[j]
		j += 1
		# print("s = ", s)  #DELME
	if s == num:
		break

print("i = {}, j = {}".format(i, j))
print("sum of min and max of nums[i:j] = ", min(all_nums[i:j]) + max(all_nums[i:j]))









