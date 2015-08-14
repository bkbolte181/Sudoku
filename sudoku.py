'''
Solve any valid sudoku puzzle or alert if it is invalid
'''

import copy
import time

def solve(puzzle=[[]]):
	''' Solve the puzzle '''
	# Check to make sure the puzzle is valid
	for ik, iv in enumerate(puzzle):
		for jk, jv in enumerate(iv):
			if not check(puzzle=puzzle, row=ik, column=jk, value=puzzle[ik][jk]):
				print 'Invalid puzzle'
				return puzzle
	
	square = 0
	total_length = len([j for i in puzzle for j in i])
	
	possibilities = [[] for i in range(0, total_length)]
	
	permanent_puzzle = copy.deepcopy(puzzle)
	
	# Generate possibilities for the first square
	possibilities[0] = populate_possibilities(puzzle=puzzle, square=0)
	
	while square < total_length and square > -1:
		row = square / len(puzzle)
		column = square % len(puzzle[row])
		if len(possibilities[square]) == 0:
			puzzle[row][column] = permanent_puzzle[row][column]
			square = square - 1
		else:
			puzzle[row][column] = possibilities[square].pop(0)
		
			# Generate possibilities for the next square (if there is a next square)
			if square + 1 < total_length:
				possibilities[square + 1] = populate_possibilities(puzzle=puzzle, square=square + 1)
			
			square = square + 1
#  		nice_print(puzzle)
#  		time.sleep(0.5)
	return puzzle

def populate_possibilities_old(puzzle=[], square=-1, row=0, column=0):
	''' Find all possible values for a given square and puzzle - old way, where each value was checked '''
	if square != -1:
		row = square / len(puzzle)
		column = square % len(puzzle[row])
	possibilities = []
	for i in range(1,10):
		if check(puzzle=puzzle, column=column, row=row, value=i):
			possibilities.append(i)
	return possibilities

def populate_possibilities(puzzle=[], square=-1, row=0, column=0):
	''' Find all possible values for a given square and puzzle - noticeably faster and better '''
	if square != -1:
		row = square / len(puzzle)
		column = square % len(puzzle[row])
	possibilities = []
	if puzzle[row][column] != 0:
		# If there is already a value for that spot
		return [puzzle[row][column],]
	else:
		# Main logic (basically the same as the "check" function)
		c = [i[column] for i in puzzle]
		r = puzzle[row]
		s = [j for (y, i) in enumerate(puzzle) for (x, j) in enumerate(i) if x/3 == column/3 and y/3 == row/3]
		items = list(i for i in set(c+r+s) if i != 0)
		return [i for i in range(1,10) if not i in items]

def check(puzzle=[], column=0, row=0, value=0):
	''' Checks a value at a location '''
	if puzzle[row][column] != 0:
		return puzzle[row][column] == value
	c = [i[column] for i in puzzle]
	r = puzzle[row]
	s = [j for (y, i) in enumerate(puzzle) for (x, j) in enumerate(i) if x/3 == column/3 and y/3 == row/3]
	items = list(i for i in set(c+r+s) if i != 0)
	return not value in items # True if value can be used, False if value can't be used

def nice_print(puzzle):
	''' Prints the puzzle in a prettier way '''
	num_spaces = 0
	for row in puzzle:
		for element in row:
			if type(element) is list:
				to_add = ''.join(str(x) for x in element)
			else:
				to_add = str(element)
			if len(to_add) > num_spaces:
				num_spaces = len(to_add)
	counter = 0
	for row in puzzle:
		if counter % 3 == 0:
			print ''.join('-' for i in range(0, (num_spaces+3) * 9 + 1))
		counter = counter + 1
		r = '| '
		counter2 = 0
		for element in row:
			if type(element) is list:
				to_add = ''.join(str(x) for x in element)
			elif element == 0:
				to_add = ' '
			else:
				to_add = str(element)
			r = r + ''.join(' ' for i in range(0, num_spaces - len(to_add))) + to_add
			counter2 = counter2 + 1
			if counter2 % 3 == 0:
				r = r + ' | '
			else:
				r = r + '   '
		print r
	print ''.join('-' for i in range(0, (num_spaces+3) * 9 + 1))

def main():
	''' Main method with some sample puzzles '''
# 	puzzle = [
# 		[0, 0, 0, 0, 7, 4, 3, 1, 6],
# 		[0, 0, 0, 6, 0, 3, 8, 4, 0],
# 		[0, 0, 0, 0, 0, 8, 5, 0, 0],
# 		[7, 2, 5, 8, 0, 0, 0, 3, 4],
# 		[0, 0, 0, 0, 3, 0, 0, 5, 0],
# 		[0, 0, 0, 0, 0, 2, 7, 9, 8],
# 		[0, 0, 8, 9, 4, 0, 0, 0, 0],
# 		[0, 4, 0, 0, 8, 5, 9, 0, 0],
# 		[9, 7, 1, 3, 2, 6, 4, 8, 5],
# 	]
	
# 	puzzle = [
# 		[2, 0, 0, 0, 0, 0, 0, 9, 3],
# 		[0, 0, 0, 0, 0, 0, 7, 0, 0],
# 		[0, 0, 7, 5, 8, 6, 0, 0, 0],
# 		[0, 0, 0, 1, 0, 0, 0, 2, 6],
# 		[4, 0, 1, 0, 0, 0, 0, 0, 0],
# 		[0, 0, 0, 4, 0, 3, 0, 0, 0],
# 		[0, 0, 0, 0, 0, 9, 0, 0, 8],
# 		[7, 6, 9, 0, 1, 0, 0, 0, 0],
# 		[0, 0, 0, 0, 0, 0, 3, 0, 0],
# 	]
	
	puzzle = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
	]
	
	nice_print(puzzle)
	solution = solve(puzzle=puzzle)
	nice_print(solution)
	
if __name__=='__main__':
	main()
