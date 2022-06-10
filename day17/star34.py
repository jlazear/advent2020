import numpy as np

fname = 'input.txt'
with open(fname) as f:
    init = np.array([[1 if x=='#' else 0 for x in line] for line in map(str.strip, f.readlines()) if line.strip()], dtype='uint8')

size = len(init)
num_iterations = 6
max_size = size + num_iterations*3
mid = max_size//2

space = np.zeros([max_size, max_size, max_size, max_size], dtype='uint8')

space[mid-size//2:mid+(size+1)//2, mid-size//2:mid+(size+1)//2, mid, mid] = init

def update(space, new_space=None):
    if new_space is None:
        new_space = space.copy()
    
    for i, j, k, l in np.ndindex(*space.shape):
        space_ijkl = space[i, j, k, l]
        ilow = max(i-1, 0)
        ihigh = min(i+2, space.shape[0])

        jlow = max(j-1, 0)
        jhigh = min(j+2, space.shape[1])

        klow = max(k-1, 0)
        khigh = min(k+2, space.shape[2])

        llow = max(l-1, 0)
        lhigh = min(l+2, space.shape[3])

        subspace_ijkl = space[ilow:ihigh, jlow:jhigh, klow:khigh, llow:lhigh]
        count = subspace_ijkl.sum() - space_ijkl
        if space_ijkl == 1:
            new_space[i, j, k, l] = 1 if (count in (2, 3)) else 0
        else:
            new_space[i, j, k, l] = 1 if (count == 3) else 0
    return new_space, space

new_space = None
for i in range(num_iterations):
    print('-'*10)
    space, new_space = update(space, new_space)
    print("i = ", i)

print("number active = ", space.sum())
