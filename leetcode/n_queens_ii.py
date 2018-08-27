class Solution(object):
    def totalNQueens(self, n, row=0, cols=0, diag_a=0, diag_b=0):
        if row == n:
            return 1
        sols = 0
        for c in xrange(n):
            if cols & 1 << c:
                continue
            if diag_a & 1 << (row + c):
                continue
            if diag_b & 1 << ((row - c) + n):
                continue
            sols += self.totalNQueens(n, row + 1, cols | 1 << c,
                                      diag_a | 1 << (row + c),
                                      diag_b | 1 << ((row - c) + n))
        return sols
        
