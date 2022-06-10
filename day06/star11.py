def parse_answers(answers):
	answers = answers.replace('\n', '')
	s = set(answers)
	return s

answer_list = []
with open('input.txt') as f:
	groups = f.read().split('\n\n')

for group in groups:
	answer_list.append(len(parse_answers(group)))

print("answer_list = ", answer_list)
print("sum = ", sum(answer_list))

	