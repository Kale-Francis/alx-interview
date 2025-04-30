#!/usr/bin/python3
"""
Pascal`s Triangle implimentation
"""

def pascal_triangle(n):
	"""
	Returns a list of lists of integers represnting the pascal`s triangle
	"""

	if n <= 0:
		return[]
		
	triangle = [[1]] #first row

	for i in range(1, n):
		prev_row = triangle[-1]
		row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(lenprev_row) - 1)] + [1]
		triangle.append(row)

	return triangle
