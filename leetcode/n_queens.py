class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []
        for q_list in self.backtrack(n):
            board = [['.'] * n for _ in xrange(n)]
            for qr, qc in q_list:
                board[qr][qc] = 'Q'
            ret.append([''.join(row) for row in board])
        return ret
    
    def backtrack(self, n, row=0, cols=0, diag_a=0, diag_b=0):
        if row == n:
            return [[]]
        rets = []
        for c in xrange(n):
            if cols & 1 << c:
                continue
            if diag_a & 1 << (row + c):
                continue
            if diag_b & 1 << ((row - c) + n):
                continue
            for queens in self.backtrack(n, row + 1, cols | 1 << c,
                                         diag_a | 1 << (row + c), diag_b | 1 << ((row - c) + n)):
                rets.append([(row, c)] + queens)
        return rets
        
