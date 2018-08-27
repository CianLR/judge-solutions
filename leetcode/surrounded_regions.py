def explore(X, Y, board, x, y, safe):
    safe.add((x, y))
    for xm, ym in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        xn, yn = x + xm, y + ym
        if 0 <= xn < X and 0 <= yn < Y and board[xn][yn] == 'O' and (xn, yn) not in safe:
            explore(X, Y, board, xn, yn, safe)

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        X, Y = len(board), len(board[0])
        safe = set()
        for x in xrange(X):
            if board[x][0] == 'O' and (x, 0) not in safe:
                explore(X, Y, board, x, 0, safe)
            if board[x][Y - 1] == 'O' and (x, Y - 1) not in safe:
                explore(X, Y, board, x, Y - 1, safe)
        for y in xrange(1, Y - 1):
            if board[0][y] == 'O' and (0, y) not in safe:
                explore(X, Y, board, 0, y, safe)
            if board[X - 1][y] == 'O' and (X - 1, y) not in safe:
                explore(X, Y, board, X - 1, y, safe)
        
        for x in xrange(len(board)):
            for y in xrange(len(board[x])):
                if board[x][y] == 'O' and (x, y) not in safe:
                    board[x][y] = 'X'
        
