class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == 0:
                    matrix[x][y] = None
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] is not None:
                    continue
                matrix[x][y] = 0
                for xn in range(len(matrix)):
                    if matrix[xn][y] is not None:
                        matrix[xn][y] = 0
                for yn in range(len(matrix[x])):
                    if matrix[x][yn] is not None:
                        matrix[x][yn] = 0
        
        
