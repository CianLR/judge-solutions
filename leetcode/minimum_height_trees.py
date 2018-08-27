from collections import deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0:
            return []
        adj = [[] for _ in xrange(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        long_start, _, _ = self.bfs_furthest_node(n, adj, 0)
        long_end, dist, paths = self.bfs_furthest_node(n, adj, long_start)
        p = long_end
        for _ in xrange((dist / 2) - 1):
            p = paths[p]
        return [paths[p]] if dist % 2 else [p, paths[p]]
        
    
    def bfs_furthest_node(self, n, adj, start):
        prev = [None] * n
        prev[start] = start
        q = deque([(1, start)])
        u, d = None, None
        while q:
            d, u = q.popleft()
            for v in adj[u]:
                if prev[v] is None:
                    prev[v] = u
                    q.append((d + 1, v))
        return u, d, prev
        
