def evaluate_line(line):
    stack = []
    num = ''
    for c in line + ' ':
        if c == ' ':
            if num:
                val = int(num)
                num = ''
                if  stack and stack[-1] in '+*':
                    op = stack.pop()
                    val2 = stack.pop()
                    if op == '+':
                        stack.append(val + val2)
                    else:
                        stack.append(val * val2)
                else:
                    stack.append(val)
        elif c.isdigit():
            num += c
        elif c in '+*(':
            stack.append(c)
        elif c == ')':
            if num:
                val = int(num)
                num = ''
            else:
                val = stack.pop()
            op = stack.pop()
            while op != '(':
                val2 = stack.pop()
                val = (val + val2) if op == '+' else (val * val2)
                op = stack.pop()
            if stack and stack[-1] in '+*':
                op = stack.pop()
                val2 = stack.pop()
                if op == '+':
                    stack.append(val + val2)
                else:
                    stack.append(val * val2)
            else:
                stack.append(val)
    return stack[0]

print("sum = ", sum([evaluate_line(line) for line in open('input.txt')]))