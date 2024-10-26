from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # A clockwise rotation is equivalent to a transpose and then a horizontal reflection
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # transpose
            matrix[i].reverse() # horizontal reflection