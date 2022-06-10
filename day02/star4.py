from collections import Counter

def check_password(line):
	policy, pwd = line.split(':')
	nums, letter = policy.split(' ')
	num_min, num_max = nums.split('-')
	num_min = int(num_min)
	num_max = int(num_max)
	pwd = pwd.strip()

	at_one = (pwd[num_min-1] == letter)
	at_two = (pwd[num_max-1] == letter)
	valid = bool(at_one) ^ bool(at_two)
	return valid

num_valid = 0
num_invalid = 0
for line in open('input.txt'):
	if check_password(line):
		num_valid += 1
	else:
		num_invalid += 1

print("number of valid passwords = ", num_valid)
print("number of invalid passwords = ", num_invalid)