class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if len(A) == 0 or len(A[0]) == 0:
            return 0
        for r in range(len(A)):
            if not A[r][0]:
                self.toggle_row(A, r)
        
        for c in range(1, len(A[0])):
            toflip = 0
            for r in range(len(A)):
                toflip += -1 if A[r][c] else 1
            if toflip > 0:
                self.toggle_col(A, c)
        return sum(
            int(''.join(str(c) for c in row), 2) for row in A
        )
    
    def toggle_row(self, A, r):
        A[r] = [0 if b else 1 for b in A[r]]
    
    def toggle_col(self, A, c):
        for r in range(len(A)):
            A[r][c] = 0 if A[r][c] else 1
        
