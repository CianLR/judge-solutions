from collections import deque

class Solution(object):
    
    _memo = {}

    def shortestPathAllKeys(self, grid):
        self._memo = {}
        grid = [list(s) for s in grid]
        K, start = self.get_k_start(grid)
        return self.recur_key_order(grid, start, 0, K)

    def recur_key_order(self, grid, start, used, K):
        if used == (1 << K) - 1:
            return 0
        best_solve = -1
        for k in xrange(K):
            if used & (1 << k):
                continue
            # Get k next
            new_d, new_s = self.search(grid, start, used, k)
            if new_d == -1:
                continue
            nxt = self.recur_key_order(
                    grid, new_s, used | (1 << k), K)
            if nxt != -1:
                if best_solve == -1:
                    best_solve = nxt + new_d
                else:
                    best_solve = min(best_solve, nxt + new_d)
        return best_solve


    def search(self, grid, start, used, k):
        if (start, used, k) in self._memo:
            return self._memo[(start, used, k)]
        aord = ord('a')
        Aord = ord('A')
        key = chr(aord + k)
        seen = {start}
        q = deque([(0, start)])
        while q:
            d, (x, y) = q.popleft()
            if grid[x][y] == key:
                self._memo[(start, used, k)] = (d, (x, y))
                return d, (x, y)
            for xm, ym in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                xm += x
                ym += y
                if 0 <= xm < len(grid) and 0 <= ym < len(grid[xm]):
                    if (xm, ym) in seen:
                        continue
                    g = grid[xm][ym]
                    if g == '#':
                        continue
                    if g.isupper() and not used & (1 << (ord(g) - Aord)):
                        continue
                    seen.add((xm, ym))
                    q.append((d + 1, (xm, ym)))
        self._memo[(start, used, k)] = (-1, None)
        return -1, None


    def get_k_start(self, grid):
        char = None
        start = None
        for x, l in enumerate(grid):
            for y, c in enumerate(l):
                if c == '@':
                    start = (x, y)
                    grid[x][y] = '.'
                elif c.islower() and (char is None or ord(c) > char):
                    char = ord(c)
        return (char - ord('a')) + 1, start

    

if 0:
    s = Solution()
    print s.shortestPathAllKeys([
        "@.a.#",
        "###.#",
        "b.A.B"])
    print s.shortestPathAllKeys([
        "@..aA",
        "..B#.",
        "....b"])


