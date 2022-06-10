import numpy as np

vs = [0]
for line in open('input.txt'):
	vs.append(int(line))
vs.sort()
vs.append(vs[-1] + 3)

vs = np.array(vs)

dvs = np.diff(vs)

udvs = np.unique(dvs, return_counts=True)
print(udvs)

# only two, so multiply manually... but implement after the fact anyway

one_times_three = (udvs[1][udvs[0] == 1] * udvs[1][udvs[0] == 3])[0]
print("number of 1-jolt differences multiplied by the number of 3-jolt differences = ", one_times_three)