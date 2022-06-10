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

def validate_passport(passport_dict):
	"""Assumes the passport has all of the required fields"""
	try:
		if not (1920 <= int(passport_dict['byr']) <= 2002): return False
		if not (2010 <= int(passport_dict['iyr']) <= 2020): return False
		if not (2020 <= int(passport_dict['eyr']) <= 2030): return False
		
		hgt_units = passport_dict['hgt'][-2:]
		if hgt_units not in ('cm', 'in'):
			return False
		elif hgt_units == 'cm':
			if not (150 <= int(passport_dict['hgt'][:-2]) <= 193): return False
		else:
			if not (59 <= int(passport_dict['hgt'][:-2]) <= 76): return False

		if passport_dict['hcl'][0] != '#':
			return False
		else:
			for c in passport_dict['hcl'][1:]:
				if c not in '0123456789abcdef':
					return False
		if passport_dict['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
			return False
		if len(passport_dict['pid']) != 9:
			return False
		int(passport_dict['pid'])  # will throw an error if not a valid number
		return True
	except Error:
		return False


passport_dicts = [parse_passport_string(passport_string) for passport_string in passport_strings]

count_first_pass = 0
count_second_pass = 0
for passport_dict in passport_dicts:
	count_first_pass += 1
	if check_passport_dict_validity(passport_dict) and validate_passport(passport_dict):
		count_second_pass += 1

print("number of valid modified passports = ", count_first_pass)
print("number of totally validated passports = ", count_second_pass)
