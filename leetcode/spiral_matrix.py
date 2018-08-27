class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in xrange(R)]
        loc = (0, 0)
        direc = 0
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        path = []
        while self.in_bounds(loc, R, C) and not seen[loc[0]][loc[1]]:
            seen[loc[0]][loc[1]] = True
            path.append(matrix[loc[0]][loc[1]])
            new_loc = self.vec_add(loc, DIRS[direc])
            if not self.in_bounds(new_loc, R, C) or seen[new_loc[0]][new_loc[1]]:
                direc = (direc + 1) % 4
                new_loc = self.vec_add(loc, DIRS[direc])
            loc = new_loc
        return path
    
    def in_bounds(self, loc, R, C):
        return 0 <= loc[0] < R and 0 <= loc[1] < C
    
    def vec_add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))
        
        
