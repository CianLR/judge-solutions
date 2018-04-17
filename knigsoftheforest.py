import heapq

def get_king_year(start_moose, rest):
    queue = [(s, y, k) for y, s, k in start_moose]
    heapq.heapify(queue)
    s, y, k = heapq.heappop(queue)
    if k:
        return y
    for y, s, k in rest:
        stren, year, iskarl = heapq.heappushpop(queue, (s, y, k))
        if iskarl:
            return y
    return 'unknown'

def main():
    K, N = [int(x) for x in input().split()]
    ky, ks = [int(x) for x in input().split()]
    moose = [tuple(int(x) for x in input().split()) for _ in range(K + N - 2)]
    allmoose = sorted([(y, -s, False) for y, s in moose] + [(ky, -ks, True)])
    start_moose, rest = allmoose[:K], allmoose[K:]
    print(get_king_year(start_moose, rest))

if __name__ == '__main__':
    main()

