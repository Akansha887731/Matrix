"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

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

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

"""
Please upvote if you like the solution :)
Intuition
The code checks if a given Sudoku board is valid or not. A valid Sudoku board must satisfy the following conditions:

Each row must have unique values from 1 to 9.
Each column must have unique values from 1 to 9.
Each of the 9 subgrids (3x3) must have unique values from 1 to 9.

Approach
The code uses sets to keep track of the values in each row, column, and subgrid. It iterates through each cell in the Sudoku board, checking whether the current value violates any of the three conditions mentioned above. If it finds a violation, it returns False; otherwise, it adds the value to the corresponding sets for the row, column, and subgrid. If the entire board is traversed without finding any violations, the function returns True.

Complexity
Time complexity:
Let's denote the size of the Sudoku board as N (which is 9 in this case). The code iterates through each cell in the N x N board, performing constant-time operations for each cell. Therefore, the time complexity is O(N^2).

Space complexity:
The space complexity is O(N^2) as well. The code uses sets to store values for each row, column, and subgrid. The sizes of these sets are proportional to the size of the board, and since there are three types (row, column, subgrid), the space complexity is O(N^2).
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row , column = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}, {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        block = {(0, 0): set(), (0, 1): set(), (0, 2): set(), (1, 0): set(), (1, 1): set(), (1, 2): set(), (2, 0): set(), (2, 1): set(), (2, 2): set()}
        length = len(board)
        red_flag = False
        for i in range(length):
            for j in range(length):
                value = board[i][j]
                if value == ".":
                    continue
                if value in row.get(i) or value in column.get(j) or value in block[(i//3, j//3)]:
                    return False
                else:
                    row[i].add(value)
                    column[j].add(value)
                    block[(i//3, j//3)].add(value)
        return True
                    
