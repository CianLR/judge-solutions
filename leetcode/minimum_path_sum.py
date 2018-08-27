class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        R, C = len(grid), len(grid[0])
        path_grid = [[None] * C for _ in xrange(R)]
        path_grid[0][0] = grid[0][0]
        for c in xrange(1, C):
            path_grid[0][c] = path_grid[0][c - 1] + grid[0][c]
        for r in xrange(1, R):
            path_grid[r][0] = path_grid[r - 1][0] + grid[r][0]
        for r in xrange(1, R):
            for c in xrange(1, C):
                path_grid[r][c] = grid[r][c] + min(path_grid[r - 1][c], path_grid[r][c - 1])
        return path_grid[-1][-1]
        
