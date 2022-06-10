import numpy as np

lines = [line for line in open('input.txt')]

t0 = int(lines[0])
buses = [int(item) for item in lines[1].split(',') if item != 'x']

dts = [np.ceil(t0/bus)*bus - t0 for bus in buses]

mindt = np.min(dts)
argmindt = np.argmin(dts)

print(int(buses[argmindt]*mindt))


