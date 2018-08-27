
MAX_N = 10000
left_pair = [-1] * MAX_N
right_pair = [-1] * MAX_N

def dfs(adj, u, visited):
    visited[u] = True
    for v in adj[u]:
        if left_pair[v] == -1 or (not visited[left_pair[v]] and
                                  dfs(adj, left_pair[v], visited)):
            left_pair[v] = u
            right_pair[u] = v
            return True
    return False

def kuhn(N, adj):
    for u in range(N):
        if right_pair[u] == -1:
            if not dfs(adj, u, [False] * N):
                return False
    return True

def main():
    N, M = [int(x) for x in input().split()]
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = input().split()
        adj[int(a)].append(int(b))
    print("YES" if kuhn(N, adj) else "NO")

if __name__ == '__main__':
    main()


