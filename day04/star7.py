with open('input.txt') as f:
	passport_strings = f.read().split('\n\n')

passport_strings = [s.replace('\n', ' ') for s in passport_strings]

def parse_passport_string(passport_string):
	passport_string = passport_string.replace('\n', ' ')
	pairs = passport_string.split(' ')
	d = {}
	for pair in pairs:
		if pair:
			key, value = pair.split(':')
			d[key] = value
	return d

def check_passport_dict_validity(passport_dict):
	if len(passport_dict) <= 6:
		return False
	elif len(passport_dict) == 7:
		if 'cid' in passport_dict:
			return False
		else:
			return True
	else:
		return True

passport_dicts = [parse_passport_string(passport_string) for passport_string in passport_strings]

count = 0
for passport_dict in passport_dicts:
	if check_passport_dict_validity(passport_dict):
		count += 1

print("number of valid modified passports = ", count)

