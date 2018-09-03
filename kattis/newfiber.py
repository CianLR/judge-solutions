
def gen_graph(N, degree):
    expected_degree = [1] * N
    degree_left = N - 2
    for i, d in sorted(enumerate(degree), key=lambda x: x[1]):
        d -= 1
        if d >= degree_left:
            expected_degree[i] += degree_left
            break
        expected_degree[i] += d
        degree_left -= d
    connections = []
    curr_degree = [0] * N
    unsatisfied = []
    for u, _ in sorted(enumerate(expected_degree), reverse=True, key=lambda x: x[1]):
        still_unsat = []
        if unsatisfied:
            v = unsatisfied.pop()
            connections.append((u, v))
            curr_degree[v] += 1
            curr_degree[u] += 1
            if curr_degree[v] < expected_degree[v]:
                still_unsat.append(v)
        if curr_degree[u] < expected_degree[u]:
            still_unsat.append(u)
        unsatisfied.extend(still_unsat)
    return sum(a != b for a, b in zip(degree, expected_degree)), connections

def main():
    N, M = map(int, raw_input().split())
    degree = [0] * N
    for _ in xrange(M):
        a, b = [int(x) for x in raw_input().split()]
        degree[a] += 1
        degree[b] += 1
    k, graph = gen_graph(N, degree)
    print k
    print N, N - 1
    for a, b in graph:
        print a, b

if __name__ == '__main__':
    main()
