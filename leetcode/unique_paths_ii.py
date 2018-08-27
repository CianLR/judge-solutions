class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        sum_grid = [[1] * len(obstacleGrid[0]) for _ in xrange(len(obstacleGrid))]
        for x in xrange(len(sum_grid)):
            for y in xrange(len(sum_grid[x])):
                if x == 0 and y == 0:
                    continue
                if obstacleGrid[x][y]:
                    sum_grid[x][y] = 0
                else:
                    sum_grid[x][y] = ((sum_grid[x-1][y] if x > 0 else 0) +
                                      (sum_grid[x][y-1] if y > 0 else 0))
        return sum_grid[-1][-1]
        
