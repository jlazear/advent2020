def parse_rule_line(line):
    field, rule_str = line.split(':')
    field = field.strip()
    rules = rule_str.split(' or ')
    rules2 = []
    for rule in rules:
        rules2.append([int(x) for x in rule.split('-')])
    return field, rules2

def find_invalid_sum(nearby, rule_set):
    invalids = [x for x in nearby if x not in rule_set]
    return sum(invalids)

d = {}
yours = []

with open('input.txt') as f:
    s = f.read()

rules_str, your_str, nearby_str = s.split('\n\n')

rules_list = rules_str.split('\n')
for line in rules_list:
    field, rules = parse_rule_line(line)
    d[field] = rules

rule_set = set()
for field, rules in d.items():
    for low, high in rules:
        for x in range(low, high+1):
            rule_set.add(x)

error_rate = 0
for line in nearby_str.split('\n')[1:]:
    if line:
        nearby = [int(x) for x in line.split(',')]
        error_rate += find_invalid_sum(nearby, rule_set)

print("error rate = ", error_rate)