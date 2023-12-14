"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

"""
Intuition
The intuition behind this solution is to traverse the given matrix in a spiral order. Starting from the outermost layer, the algorithm iterates through each layer, extracting elements in a clockwise direction, until the entire matrix is covered.

Approach
Initialize four pointers (last_i, last_j, last_reverse_i, last_reverse_j) to represent the boundaries of the current layer being processed.
Use a while loop to iterate through the matrix while the boundaries are valid (i.e., last_reverse_j <= last_j and last_i <= last_reverse_i).
Inside the loop, use four for loops to traverse the top row, right column, bottom row, and left column of the current layer.
Adjust the pointers accordingly after traversing each side.
Continue the process until all layers are traversed.
Complexity
Time complexity:
The time complexity is O(m * n), where m is the number of columns and n is the number of rows in the matrix. This is because the algorithm iterates through each element in the matrix exactly once.

Space complexity:
The space complexity is O(1) because the algorithm uses a constant amount of extra space to store the result (l) regardless of the input size. The space used for the pointers is also constant.
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix[0])
        n = len(matrix)
        l = []
        last_i, last_j = 0, m-1

        last_reverse_i, last_reverse_j = n-1, 0

        while last_reverse_j <= last_j and last_i <= last_reverse_i:
            
            for p in range(last_reverse_j, last_j + 1):
                l.append(matrix[last_i][p])
            last_i += 1
                
            for q in range(last_i, last_reverse_i + 1):
                l.append(matrix[q][last_j])
            last_j -= 1

            if last_i <= last_reverse_i:
                for y in range(last_j, last_reverse_j - 1  , -1):
                    l.append(matrix[last_reverse_i][y])
                last_reverse_i -= 1

            
            if last_reverse_j <= last_j:
                for z in range(last_reverse_i , last_i -1 , -1):
                    l.append(matrix[z][last_reverse_j])
                last_reverse_j += 1
        return l
