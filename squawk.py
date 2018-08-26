
def main():
    N, M, S, T = [int(x) for x in raw_input().split()]
    adj_list = [[] for _ in xrange(N)]
    for _ in xrange(M):
        a, b = [int(x) for x in raw_input().split()]
        adj_list[a].append(b)
        adj_list[b].append(a)

    got_last = [0] * N
    got_last[S] = 1
    for _ in xrange(T):
        next_got_last = [0] * N
        for u in xrange(N):
            if got_last[u] == 0:
                continue
            for v in adj_list[u]:
                next_got_last[v] += got_last[u]
        got_last = next_got_last
    print sum(got_last)

if __name__ == '__main__':
    main()

