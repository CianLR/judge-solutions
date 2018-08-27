from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj = defaultdict(list)
        for a, b in tickets:
            adj[a].append(b)
        for k in adj:
            adj[k] = sorted(adj[k], reverse=True)
        
        path = []
        self.find_euler_path('JFK', adj, path)
        return path[::-1]
    
    def find_euler_path(self, u, adj, path):
        while adj[u]:
            v = adj[u].pop()
            self.find_euler_path(v, adj, path)
        path.append(u)
            
        
