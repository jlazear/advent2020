def apply_mask(value, mask):
    bvalue = "{:036b}".format(value)
    blist = [c for c in bvalue]
    for i in range(len(bvalue)):
        m = mask[i]
        if m == 'X':
            continue
        blist[i] = m
    return int('0b' + ''.join(blist), 2)


commands = [line.strip() for line in open('input.txt')]
d = {}
mask = ''
for command in commands:
    words = command.split('=')
    if words[0].strip() == 'mask':
        mask = words[1].strip()
    else:
        memloc = int(words[0].split('[')[1].strip(' ]'))
        value = int(words[1])
        newvalue = apply_mask(value, mask)
        d[memloc] = newvalue

print(sum(d.values()))

