import sys
from collections import deque

sys.setrecursionlimit(10000)

class Node:
    def __init__(self, i):
        self.i = i
        self.adj = []

    def add_adj(self, k):
        self.adj.append(k)

def dfs(seen, u, _memo={}):
    if u.i in _memo:
        return _memo[u.i]
    for v in u.adj:
        if v.i in seen or dfs(seen | {v.i}, v):
            _memo[v.i] = True
            return True
    _memo[u.i] = False
    return False

def cycle(start):
    return dfs({start}, start)

def main():
    N = int(sys.stdin.readline())
    cities = {}
    for _ in range(N):
        a, b = sys.stdin.readline().split()
        if a not in cities:
            cities[a] = Node(len(cities))
        if b not in cities:
            cities[b] = Node(len(cities))
        cities[a].add_adj(cities[b])

    city = sys.stdin.readline().strip()
    while city:
        print(city, "safe" if cycle(cities[city]) else "trapped")
        city = sys.stdin.readline().strip()

if __name__ == '__main__':
    main()

