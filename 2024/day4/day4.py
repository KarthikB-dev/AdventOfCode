import re
import pdb
from icecream import ic
rows = []
with open(input(), "r+") as fin:
	rows = fin.readlines()

columns = []
for col in range(len(rows[0]) - 1):
	curr_col = ""
	for row in range(len(rows)):
		curr_row = rows[row]
		curr_col += curr_row[col]
	columns.append(curr_col)
		
# Store the diagonals of the input, starting from
# the top right to the bottom left, where additional
# characters are appending by moving down and right
# while staying in the bounds of the input

# Move the starting index left at first
diags = []
row, col = 0, len(rows[0]) - 1
while (col >= 0):
	# While in bounds, accumulate characters by moving
	# down and right
	curr_diag = ""
	curr_col = col
	curr_row = row
	while (curr_row < len(rows) and curr_col < len(rows[curr_row])):
		curr_diag += rows[curr_row][curr_col]
		curr_row += 1
		curr_col += 1
	diags.append(curr_diag)
	col -= 1

# Then move the start down when the leftmost column
# is reached
row, col = 0, len(rows[0]) - 1
while (row < len(rows)):
	# While in bounds, accumulate characters by moving
	# down and right
	curr_diag = ""
	curr_col = col
	curr_row = row
	while (curr_row < len(rows) and curr_col < len(rows[curr_row])):
		curr_diag += rows[curr_row][curr_col]
		curr_row += 1
		curr_col += 1
	diags.append(curr_diag)
	row += 1

# Match rows, columns, and diagonals for the patterns
# ".*x.*m.*a.*s" and ".*s.*a.*m.*x" to find these in both
# directions
num_xmas = 0

# New algo: find all instances of the letter x
# then, find all occurrences of m after it
# then, find all occurrences of a after each of these individual instances
# then, find all occurrecnes of s after each of these individual instances
def count_xmas(pos_dict):
	x_pos = []
	# Get the positions of X chars
	for k,v in pos_dict.items():
		if v == 'X':
			x_pos.append(k)
	# Tuple list of X chars and M chars that 
	# appear after it
	xm = []
	for xp in x_pos:
		for k,v in pos_dict.items():
			if v == 'M' and k > xp:
				xm.append((xp, k))
	# Add A to the tuple
	xma = []
	for curr in xm:
		for k,v in pos_dict.items():
			if v == 'A' and k > curr[1]:
				xma.append(curr + (k,))
	# Add S to the tuple
	xmas = []
	for curr in xma:
		for k,v in pos_dict.items():
			if v == 'S' and k > curr[2]:
				xma.append(curr + (k,))
	return(len(xmas))

# More efficient algorithm
# Create a data structure storing how many times a given letter
# appears at or after some index, e.g. if we have
# XMAXSS
# X: {0:2, 1:1, 2:1, 3:1, 4:0, 5:0}
# M: {0:1, 1:1, 2:0, 3:0, 4:0, 5:0}
# A: {0:1, 1:1, 2:1, 3:0, 4:0, 5:0}
# S: {0:2, 1:2, 2:2, 3:2, 4:1, 5:0}
# Create time: O(n^2)
# Then, using this data structure, compute the following:
# \sigma i_x : M[i+1] * A[i+2] * S[i+3] where i+3 < len(row/col/diag)
# sum up all these values for all of the places where this might 
# be found
def fast_xmas(pos_dict):
	x_pos = []
	md = {}
	ad = {}
	sd = {}
	num_xmas = 0
	# Compute the data structures using the 
	# pos_dict
	for p, c in pos_dict.items():
		if c == 'X':
			x_pos.append(p)			
		md[p] = 0
		ad[p] = 0
		sd[p] = 0
	# Compute md, ad, sd
	for p, c in pos_dict.items():
		if c == 'M':
			for p2 in range(p, len(pos_dict)):
				md[p2] += 1
		if c == 'A':
			for p2 in range(p, len(pos_dict)):
				ad[p2] += 1
		if c == 'S':
			for p2 in range(p, len(pos_dict)):
				sd[p2] += 1
	# Compute the final sum
	for xp in x_pos:
		if xp + 3 < len(pos_dict):
			num_xmas += md[xp+1] * ad[xp+2] * sd[xp+3]

	return num_xmas

# Reverse each string and repeat the above
for c in columns:
	fmatches = re.findall(r".*X.*M.*A.*S", c)
	rmatches = re.findall(r".*S.*A.*M.*X", c)
	if (len(fmatches)):
		print('Columns:')
		ic(fmatches)
	if (len(rmatches)):
		print('Columns')
		ic(rmatches)
	if (len(rmatches) or len(fmatches)):
		# Maps position to letter
		ic(num_xmas)
		pos_dict = dict(enumerate(c))
		num_xmas += fast_xmas(pos_dict)
		rev_c = c[::-1]
		pos_dict = dict(enumerate(rev_c))
		num_xmas += fast_xmas(pos_dict)
		ic(num_xmas)

for r in rows:
	fmatches = re.findall(r".*X.*M.*A.*S", r)
	rmatches = re.findall(r".*S.*A.*M.*X", r)
	if (len(fmatches)):
		print('Rows:')
		ic(fmatches)
	if (len(rmatches)):
		print('Rows:')
		ic(rmatches)
	if (len(fmatches) or len(rmatches)):
		pos_dict = dict(enumerate(r))
		num_xmas += fast_xmas(pos_dict)
		rev_r = r[::-1]
		pos_dict = dict(enumerate(rev_r))
		num_xmas += fast_xmas(pos_dict)	

for d in diags:
	fmatches = re.findall(r".*X.*M.*A.*S", d)
	rmatches = re.findall(r".*S.*A.*M.*X", d)
	if (len(fmatches)):
		print('Diags')
		ic(fmatches)
	if (len(rmatches)):
		print('Diags')
		ic(rmatches)
	if (len(fmatches) or len(rmatches)):
		pos_dict = dict(enumerate(d))
		num_xmas += fast_xmas(pos_dict)
		rev_d = d[::-1]
		pos_dict = dict(enumerate(rev_d))
		num_xmas += fast_xmas(pos_dict)

print(num_xmas)