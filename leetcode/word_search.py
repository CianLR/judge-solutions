from collections import defaultdict

class Node:
    def __init__(self, c):
        self.c = c
        self.seen = False
        self.adj = defaultdict(list)
    
    def search(self, word, s=0):
        if s == len(word):
            return True
        self.seen = True
        for v in self.adj[word[s]]:
            if not v.seen and v.search(word, s + 1):
                return True
        self.seen = False
        return False

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        root = Node('')
        node_grid = [[None] * len(board[0]) for _ in xrange(len(board))]
        for r in xrange(len(board)):
            for c, val in enumerate(board[r]):
                u = Node(val)
                node_grid[r][c] = u
                root.adj[val].append(u)
                if r > 0:
                    v = node_grid[r - 1][c]
                    v.adj[val].append(u)
                    u.adj[v.c].append(v)
                if c > 0:
                    v = node_grid[r][c - 1]
                    v.adj[val].append(u)
                    u.adj[v.c].append(v)
        return root.search(word)
    
        
