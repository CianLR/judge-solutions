from collections import deque

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if N == 0:
            return True
        adj = [[] for _ in xrange(N)]
        for a, b in dislikes:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)
        colour = [None] * N
        stack = deque([0])
        colour[0] = True
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if colour[u] == colour[v]:
                    return False
                if colour[v] is None:
                    colour[v] = not colour[u]
                    stack.append(v)
        return True
        
