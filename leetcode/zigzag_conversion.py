class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) < 3 or numRows == 1:
            return s
        grid = [[''] * len(s) for _ in range(numRows)]
        c = x = y = 0
        while c < len(s):
            while y < numRows - 1 and c < len(s):
                grid[y][x] = s[c]
                c += 1
                y += 1
            while y > 0 and c < len(s):
                grid[y][x] = s[c]
                y -= 1
                x += 1
                c += 1
        #for r in grid:
        #    print(''.join(c if c else ' ' for c in r))
        return ''.join(''.join(r) for r in grid)
        
