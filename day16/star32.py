
def parse_rule_line(line):
    field, rule_str = line.split(':')
    field = field.strip()
    rules = rule_str.split(' or ')
    rules_set = set()
    for rule in rules:
        low, high = map(int, rule.split('-'))
        for x in range(low, high+1):
            rules_set.add(x)
    return field, rules_set

def find_invalid_sum(nearby, rule_set):
    invalids = [x for x in nearby if x not in rule_set]
    return sum(invalids)

d = {}
valid_tickets = []

fname = 'input.txt'
with open(fname) as f:
    s = f.read()

rules_str, your_str, nearby_str = s.split('\n\n')

rules_list = rules_str.split('\n')
for line in rules_list:
    field, rule_set = parse_rule_line(line)
    d[field] = rule_set

rule_set = set.union(*d.values())
    

error_rate = 0
for line in nearby_str.split('\n')[1:]:
    if line:
        nearby = [int(x) for x in line.split(',')]
        invalid_sum = find_invalid_sum(nearby, rule_set)
        if not invalid_sum:
            valid_tickets.append(nearby)


positions = [set() for _ in range(len(valid_tickets[0]))]

for ticket in valid_tickets:
    for i in range(len(ticket)):
        value = ticket[i]
        positions[i].add(value)

d_valids = {key: [] for key in d.keys()}

for key in d_valids.keys():
    rules = d[key]
    for i in range(len(positions)):
        pos_set = positions[i]
        if pos_set <= rules:
            d_valids[key].append(i)

available_positions = list(range(len(positions)))
field_assignments = {}

while available_positions:
    for key, value in d_valids.items():
        if len(value) == 1:
            val0 = value[0]
            field_assignments[val0] = key
            available_positions.remove(val0)
            for _, positions in d_valids.items():
                try:
                    positions.remove(val0)
                except ValueError:
                    pass

yours = [int(x) for x in your_str.split('\n')[1].split(',')]

your_dict = {field_assignments[i]: yours[i] for i in range(len(yours))}

answer = 1
for x in [value for key, value in your_dict.items() if key.startswith('departure')]:
    answer *= x

print("answer = ", answer)
