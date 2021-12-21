'''
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.

'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking horizontal rows
        valid = True
        for row in board:
            trimmed_num = [int(num) for num in row if num.isdigit()]
            # if any of the digits in the row are > 9
            if any((x > 9 for x in trimmed_num)):
                valid = False
                break
            # if the row contains duplicate numbers
            if len(set(trimmed_num)) != len(trimmed_num):
                valid = False
                break

        # if above test is pass, checking vertical rows
        if valid:
            # transpose the matrix
            board_t = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
            for row in board_t:
                trimmed_num = [int(num) for num in row if num.isdigit()]
                if any((x > 9 for x in trimmed_num)):
                    valid = False
                    break
                if len(set(trimmed_num)) != len(trimmed_num):
                    valid = False
                    break

        # if above test is pass, check for individual 3X3 matrix to be valid
        if valid:
            for k in range(3):
                for i in range(3):
                    row = []
                    h_shft = i*3
                    for j in range(3):
                        v_shft = j*1 + k*3
                        row += board[v_shft][h_shft:h_shft+3]
                        trimmed_num = [int(num) for num in row if num.isdigit()]
                        if any((x > 9 for x in trimmed_num)):
                            valid = False
                            break
                        if len(set(trimmed_num)) != len(trimmed_num):
                            valid = False
                            break

        return valid