def make_stack(line):
    stack = []
    num = ''
    for c in line + ' ':
        if c == ' ':
            if num:
                val = int(num)
                num = ''
                stack.append(val)
        elif c == ')':
            if num:
                val = int(num)
                num = ''
                stack.append(val)
            stack.append(c)
        elif c.isdigit():
            num += c
        elif c in '+*(':
            stack.append(c)
    return stack


def evaluate_stack(stack):
    did_something = True
    while len(stack) > 1 and did_something:
        did_something = False

        # search for parentheses
        found = True
        while found:
            found = False
            for i, c in enumerate(stack):
                if c == '(':
                    found = True
                    did_something = True
                    stack = stack[:i] + evaluate_stack(stack[i+1:])
                    break
                elif c == ')':
                    val = evaluate_stack(stack[:i])[0]
                    stack = [val] + stack[i+1:]
                    return stack

        # search for + operators
        found = True
        while found:
            found = False
            for i, c in enumerate(stack):
                if c == '+':
                    found = True
                    did_something = True
                    newstack = [stack[i-1] + stack[i+1]]
                    if i > 1:
                        newstack = stack[:i-1] + newstack
                    if i < len(stack) - 2:
                        newstack = newstack + stack[i+2:]
                    stack = newstack
                    break
 
        # search for * operators
        found = True
        while found:
            found = False
            for i, c in enumerate(stack):
                if c == '*':
                    newstack = [stack[i-1] * stack[i+1]]
                    if i > 1:
                        newstack = stack[:i-1] + newstack
                    if i < len(stack) - 2:
                        newstack = newstack + stack[i+2:]
                    stack = newstack
                    found = True
                    did_something = True
                    break
    return stack
                
print("sum = ", sum([evaluate_stack(make_stack(line))[0] for line in open('input.txt')]))