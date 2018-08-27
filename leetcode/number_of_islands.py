from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        seen = [[False] * len(grid[0]) for _ in range(len(grid))]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if seen[x][y] or grid[x][y] == '0':
                    continue
                islands += 1
                stack = deque([(x, y)])
                while stack:
                    xn, yn = stack.pop()
                    for xm, ym in self.adj(xn, yn, len(grid), len(grid[x])):
                        if not seen[xm][ym] and grid[xm][ym] == '1':
                            seen[xm][ym] = True
                            stack.append((xm, ym))
        return islands
                
    def adj(self, x, y, X, Y):
        if x - 1 >= 0:
            yield x - 1, y
        if y - 1 >= 0:
            yield x, y - 1
        if x + 1 < X:
            yield x + 1, y
        if y + 1 < Y:
            yield x, y + 1


