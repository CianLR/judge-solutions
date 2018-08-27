import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        adj = [[] for _ in xrange(n)]
        for u, v, c in flights:
            adj[u].append((v, c))
        return self.dijkstra(n, adj, src, dst, K + 1)

    def dijkstra(self, N, adj, start, dest, mxlen):
        pq = [(0, 0, start)]
        costhops = [[-1] * N for _ in xrange(mxlen + 1)]
        costhops[0][start] = 0
        while pq:
            c, h, u = heapq.heappop(pq)
            if u == dest:
                return c
            if costhops[h][u] < c or h == mxlen:
                continue
            for v, hc in adj[u]:
                if costhops[h + 1][v] != -1 and costhops[h + 1][v] <= c + hc:
                    continue
                costhops[h + 1][v] = c + hc
                heapq.heappush(pq, (c + hc, h + 1, v))
        return -1

