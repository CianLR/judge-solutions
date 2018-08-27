
class REPiece(object):
    def __init__(self, char, is_rep):
        self.char = char
        self.is_rep = is_rep

    def match(self, c):
        return c == self.char or self.char == '.'

class Solution(object):
    def isMatch(self, s, p):
        p = self.build_pieces(p)
        memo = [[None] * len(s) for _ in xrange(len(p))]
        return self.match(s, p, 0, 0, memo)
    
    def match(self, S, P, s, p, memo):
        if s == len(S):
            return p == len(P) or (
                    P[p].is_rep and self.match(S, P, s, p + 1, memo))
        if p == len(P):
            return False
        if memo[p][s] is not None:
            return memo[p][s]
        # Do matching
        if P[p].is_rep and self.match(S, P, s, p + 1, memo):
            memo[p][s] = True
        elif not P[p].match(S[s]):
            memo[p][s] = False
        elif P[p].is_rep and self.match(S, P, s + 1, p, memo):
            memo[p][s] = True
        elif self.match(S, P, s + 1, p + 1, memo):
            memo[p][s] = True
        else:
            memo[p][s] = False
        return memo[p][s]
    
    def build_pieces(self, p):
        pieces = []
        for i in xrange(len(p)):
            if p[i] == '*':
                continue
            is_rep = (i + 1 < len(p)) and p[i + 1] == '*'
            pieces.append(REPiece(p[i], is_rep))
        return pieces


