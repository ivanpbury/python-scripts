def solve(puzzle):
    row, col = find_empty(puzzle)
    if row == None:
        return True

    for num in range(1, 10):
        if is_valid(puzzle, num, row, col):
            puzzle[row][col] = num
            if solve(puzzle):
                return True
            else:
                puzzle[row][col] = 0
    return False              

def find_empty(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None, None

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    return True






puzzle = [[0, 0, 0, 5, 0, 7, 0, 0, 0], 
[0, 0, 2, 4, 0, 6, 3, 0, 0], 
[0, 9, 0, 0, 1, 0, 0, 2, 0], 
[2, 7, 0, 0, 0, 0, 0, 6, 8], 
[0, 0, 3, 0, 0, 0, 1, 0, 0], 
[1, 4, 0, 0, 0, 0, 0, 9, 3], 
[0, 6, 0, 0, 4, 0, 0, 5, 0], 
[0, 0, 9, 2, 0, 5, 6, 0, 0], 
[0, 0, 0, 9, 0, 3, 0, 0, 0]]
if solve(puzzle):
    for i in puzzle:
        print(' '.join([str(j) for j in i]))
else:
    print('Invalid puzzle')