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

def test(message, valid42s, valid31s):
    for valid42 in valid42s:
        len42 = len(valid42)
        break
    
    for valid31 in valid31s:
        len31 = len(valid31)
        break
    
    num42 = 0
    num31 = 0
    while message[:len42] in valid42s:
        num42 += 1
        message = message[len42:]
    while message[-len31:] in valid31s:
        num31 += 1
        message = message[:-len31]
    
    return (not message and num42 > 1 and num31 > 0 and num42 >= num31 + 1)

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

valid42s = set(generate_from_rule(42, rules))
valid31s = set(generate_from_rule(31, rules))
print(sum([test(message, valid42s, valid31s) for message in messages]))
