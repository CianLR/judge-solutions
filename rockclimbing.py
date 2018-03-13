import heapq

class Node:
    NODE_I = 0
    def __init__(self, cost):
        self.i = Node.NODE_I
        Node.NODE_I += 1
        self.cost = cost
        self.nxt = []

    def __lt__(self, other):
        return self.cost < other.cost

    def connect(self, node):
        self.nxt.append(node)

def connect_grid(grid):
    negs = set()
    start = Node(0)
    for n in grid[-1]:
        if n.cost + start.cost < 0:
            negs.add(n)
            negs.add(start)
        start.connect(n)
        n.connect(start)
    end = Node(0)
    for n in grid[0]:
        if n.cost + end.cost < 0:
            negs.add(n)
            negs.add(end)
        end.connect(n)
        n.connect(end)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i + 1 < len(grid):
                if grid[i][j].cost + grid[i + 1][j].cost < 0:
                    negs.add(grid[i][j])
                    negs.add(grid[i + 1][j])
                grid[i][j].connect(grid[i + 1][j])
                grid[i + 1][j].connect(grid[i][j])
            if j + 1 < len(grid[i]):
                if grid[i][j].cost + grid[i][j + 1].cost < 0:
                    negs.add(grid[i][j])
                    negs.add(grid[i][j + 1])
                grid[i][j].connect(grid[i][j + 1])
                grid[i][j + 1].connect(grid[i][j])
    return start, end, negs

def dijkstra(start, ends):
    pq = [(0, 0, start)]
    seen = set()
    while pq:
        max_e, cur_e, node = heapq.heappop(pq)
        if node in ends:
            return max_e
        if node in seen:
            continue
        seen.add(node)
        for next_node in node.nxt:
            if next_node in seen:
                continue
            new_cur = cur_e + next_node.cost
            heapq.heappush(pq, (max(max_e, new_cur), new_cur, next_node))

def main():
    R, C = map(int, input().split())
    input()
    grid = []
    for _ in range(R):
        grid.append([Node(int(x)) for x in input().split()])
    input()
    start, end, negs = connect_grid(grid)
    min_energy = dijkstra(start, {end} | negs)
    print(min_energy)

if __name__ == '__main__':
    main()

