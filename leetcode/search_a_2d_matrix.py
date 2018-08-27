class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix) or not len(matrix[0]):
            return False
        for row in matrix:
            if row[-1] < target:
                continue
            for r in row:
                if r == target:
                    return True
                elif r > target:
                    return False
            return False
        return False
        
