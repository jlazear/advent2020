from itertools import product

def generate_from_rule(rule_number, rules):
    rule = rules[rule_number]
    if rule in ('a', 'b'):
        return rule
    valids = []
    for subrule in rule:
        subvalids = [generate_from_rule(rule_no, rules) for rule_no in subrule]
        prods = product(*subvalids)
        valid = [''.join(prod) for prod in prods]
        valids.extend(valid)
    return valids


fname = 'input.txt'

rules = {}
messages = []

with open(fname) as f:
    line = f.readline().strip()
    while line:
        rule_no, rule = line.split(': ')
        rule_no = int(rule_no)
        if 'a' in rule or 'b' in rule:
            rules[rule_no] = rule.strip().strip('"')
        else:
            rules[rule_no] = [list(map(int, subrule.split())) for subrule in rule.split(' | ')]
        line = f.readline().strip()
    
    for line in f.readlines():
        line = line.strip()
        if line:
            messages.append(line)

valids = set(generate_from_rule(0, rules))

print(sum([bool(message in valids) for message in messages]))