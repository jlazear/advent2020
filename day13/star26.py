from math import gcd
lcm = lambda a, b: a*b//gcd(a, b)

def find_t(buses):
    blist = []
    for i, bus in enumerate(buses):
        if bus != 'x':
            blist.append((i, int(bus)))

    bus0 = blist[0][1]

    mkint = lambda n, bus0, k, bus: (n*bus0 + k) // bus
    mk = lambda n, bus0, k, bus: (n*bus0 + k) / bus
    firsts = []
    n = 1
    for k, bus in blist[1:]:
        while mkint(n, bus0, k, bus) != mk(n, bus0, k, bus):
            n += 1
        firsts.append(n*bus0)
        n = 1

    deltas = [lcm(bus0, bus) for _, bus in blist[1:]]
    print("firsts = ")
    print(firsts)

    print("deltas = ")
    print(deltas)
    print()

    f = firsts.pop()
    d = deltas.pop()
    
    N1int = lambda N, f, f1, d, d1: (f - f1 + N*d) // d1
    test = lambda N, f, f1, d, d1: (f + N*d == f1 + d1*N1int(N, f, f1, d, d1))
    while firsts:
        f1 = firsts.pop()
        d1 = deltas.pop()
        print("-"*10)  #DELME
        print("f = {}, d = {}".format(f, d))  #DELME
        print("f1 = {}, d1 = {}".format(f1, d1))  #DELME
        N = 1
        while not test(N, f, f1, d, d1):
            N += 1
        f = f + N*d
        d = lcm(d, d1)
    return f

fname = 'input.txt'
# fname = 'input_tests.txt'
row = 0
lines = [line for line in open(fname)]

for line in lines:
    print('='*40)
    print("line = ", line)
    buses = line.split(',')
    if len(buses) > 1:
        t = find_t(buses)
        print("\n##########\nt = ", t) 
    else:
        print("not a valid bus schedule")
