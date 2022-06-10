from collections import OrderedDict
nums = OrderedDict()

i = 0
for line in open('input.txt'):
	num = int(line)
	
	if i <= 24:
		if num in nums:
			nums[num] += 1
			print("WARNING: two of same number in dictionary...")
		else:
			nums[num] = 1
		i += 1
		continue

	valid = False
	for a in nums.keys():
		if num - a in nums.keys():
			valid = True
			break
	if not valid:
		print("first invalid number: {}".format(num))
		break
	else:
		nums.popitem(last=False)
		if num in nums:
			nums[num] += 1
		else:
			nums[num] = 1







