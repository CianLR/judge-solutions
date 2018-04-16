import heapq

def dijkstra(N, costs, start, end):
    pq = [(0, 0, 0)]
    dist = {(0, 0): 0}
    while pq:
        cost, node, prev_step = heapq.heappop(pq)
        if dist[(node, prev_step)] < cost:
            continue
        if node == end:
            return cost
        nxt = node - prev_step
        nxt_step = (nxt, prev_step)
        if 0 <= nxt < N and (nxt_step not in dist or dist[nxt_step] > cost + costs[nxt]):
            dist[nxt_step] = cost + costs[nxt]
            heapq.heappush(pq, (cost + costs[nxt], nxt, prev_step))
        nxt = node + prev_step + 1
        nxt_step = (nxt, prev_step + 1)
        if 0 <= nxt < N and (nxt_step not in dist or dist[nxt_step] > cost + costs[nxt]):
            dist[nxt_step] = cost + costs[nxt]
            heapq.heappush(pq, (cost + costs[nxt], nxt, prev_step + 1))
    assert False

def main():
    N = int(raw_input())
    fees = [int(raw_input()) for _ in range(N)]
    print dijkstra(N, fees, 0, N - 1)

if __name__ == '__main__':
    main()

