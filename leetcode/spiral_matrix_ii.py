class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[None] * n for _ in xrange(n)]
        loc = (0, 0)
        direc = 0
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        val = 1
        while self.in_bounds(loc, n) and not matrix[loc[0]][loc[1]]:
            matrix[loc[0]][loc[1]] = val
            val += 1
            new_loc = self.vec_add(loc, DIRS[direc])
            if not self.in_bounds(new_loc, n) or matrix[new_loc[0]][new_loc[1]]:
                direc = (direc + 1) % 4
                new_loc = self.vec_add(loc, DIRS[direc])
            loc = new_loc
        return matrix
    
    def in_bounds(self, loc, N):
        return 0 <= loc[0] < N and 0 <= loc[1] < N
    
    def vec_add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))
        
        
