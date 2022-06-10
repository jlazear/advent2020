from collections import Counter

def parse_answers(answers):
	num_people = len(answers.split('\n'))
	answers = answers.replace('\n', '')
	s = Counter(answers)
	return s, num_people

answer_list = []
with open('input.txt') as f:
	groups = f.read().split('\n\n')

for group in groups:
	group = group.rstrip('\n')
	s, num_people = parse_answers(group)
	# print("group = \n", group)  #DELME
	# print("s = ", s)  #DELME
	# print("num_people = ", num_people)  #DELME
	sub_count = 0
	for item, count in s.items():
		if count == num_people:
			sub_count += 1
	answer_list.append(sub_count)
	# print("sub_count = ", sub_count)  #DELME
	# print('-'*10)  #DELME

print("answer_list = ", answer_list)
print("sum = ", sum(answer_list))


def parse_answers2(answers):
	answers = answers.rstrip('\n')
	individual_strs = answers.split('\n')
	individuals = [set(individual_str) for individual_str in individual_strs]
	s = individuals.pop()
	for individual in individuals:
		s = s.intersection(individual)
	return s

answer_list2 = []
with open('input.txt') as f:
	groups = f.read().split('\n\n')

for group in groups:
	s = parse_answers2(group)
	answer_list2.append(len(s))

print("answer_list2 = ", answer_list2)
print("sum2 = ", sum(answer_list2))

