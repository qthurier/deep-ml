def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	result = []
	for a_row in a:
		if len(a_row) == len(b):
			result.append(sum(x*y for x, y in zip(a_row, b)))
		else:
			return -1
	return result