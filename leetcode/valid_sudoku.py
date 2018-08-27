class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.column(board) and self.row(board) and self.square(board)
    
    def column(self, board):
        for c in range(9):
            seen_mask = 0
            for r in range(9):
                if board[r][c] == '.':
                    continue
                n = 1 << int(board[r][c])
                if seen_mask & n:
                    return False
                seen_mask |= n
        return True
    
    def row(self, board):
        for r in range(9):
            seen_mask = 0
            for c in range(9):
                if board[r][c] == '.':
                    continue
                n = 1 << int(board[r][c])
                if seen_mask & n:
                    return False
                seen_mask |= n
        return True
    
    def square(self, board):
        for start_r in range(0, 9, 3):
            for start_c in range(0, 9, 3):
                seen_mask = 0
                for r in range(start_r, start_r + 3):
                    for c in range(start_c, start_c + 3):
                        if board[r][c] == '.':
                            continue
                        n = 1 << int(board[r][c])
                        if seen_mask & n:
                            return False
                        seen_mask |= n
        return True

