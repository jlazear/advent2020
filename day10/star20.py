import functools

vs = set([0])
for line in open('input.txt'):
	vs.add(int(line))

# the cache decorator doesn't seem to be working for some reason... :(
# @functools.lru_cache(max(vs))
# def count(value, vs=vs):
# 	if value == 0:
# 		return 1
# 	elif value < 0:
# 		return 0
# 	return (bool(value - 1 in vs)*count(value - 1, vs) +
# 		    bool(value - 2 in vs)*count(value - 2, vs) + 
# 		    bool(value - 3 in vs)*count(value - 3, vs))

# implement cache manually
count_cache = {0: 1}
def count(value, vs=vs):
	if value in count_cache:
		return count_cache[value]
	# if value == 0:
	# 	return 1
	elif value < 0:
		return 0
	num_ways = (bool(value - 1 in vs)*count(value - 1, vs) +
		        bool(value - 2 in vs)*count(value - 2, vs) + 
		        bool(value - 3 in vs)*count(value - 3, vs))
	count_cache[value] = num_ways
	return num_ways


print("number of ways =", count(max(vs)))