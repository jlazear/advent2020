from collections import Counter

def check_password(line):
	policy, pwd = line.split(':')
	nums, letter = policy.split(' ')
	num_min, num_max = nums.split('-')
	num_min = int(num_min)
	num_max = int(num_max)

	letter_count = Counter(pwd)
	n_letter = letter_count[letter]
	valid = (num_min <= n_letter <= num_max)
	return valid

num_valid = 0
for line in open('input.txt'):
	if check_password(line):
		num_valid += 1

print("number of valid passwords = ", num_valid)