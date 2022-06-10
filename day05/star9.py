def parse_bp(bp, num_row_bits=7):
	row_str = bp[:num_row_bits]
	col_str = bp[num_row_bits:]

	max_row = 2**num_row_bits - 1
	max_col = 2**(len(bp) - num_row_bits) - 1

	left = 0
	right = max_row
	mid = right//2
	for c in row_str:
		if c == 'F':
			right = mid
		else:
			left = mid + 1
		mid = (right + left) // 2

	left_col = 0
	right_col = max_col
	mid_col = right_col // 2
	for c in col_str:
		if c == 'L':
			right_col = mid_col
		else:
			left_col = mid_col + 1
		mid_col = (right_col + left_col) // 2


	return mid, mid_col, mid*8 + mid_col

max_seat_id = 0
for line in open('input.txt'):
	line = line.strip()
	row, col, seat_id = parse_bp(line)
	max_seat_id = max(max_seat_id, seat_id)

print("max seat id = ", max_seat_id)