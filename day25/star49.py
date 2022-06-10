def find_loop_size(target_key, subject_number=7, modulo=20201227):
    num = 1
    i = 0
    while num != target_key:
        num *= subject_number
        num %= modulo
        i += 1
    return i

def transform(subject_number, loop_size, modulo=20201227):
    num = 1
    for _ in range(loop_size):
        num = (num * subject_number) % modulo
    return num

keys = [int(line.strip()) for line in open('input.txt') if line]
# key1, key2 = 5764801, 17807724

loops = [find_loop_size(key) for key in keys]

print(loops)

encryption_keys = [transform(keys[1 - i], loops[i]) for i in range(len(keys))]

print(encryption_keys)