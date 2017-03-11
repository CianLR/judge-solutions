from queue import PriorityQueue

class Location:
    def __init__(self, i, items):
        self.i = i
        self.items = items
        self.connected_to = []

        self.best_road_to = None
        self.total_items_up_to = 0
        self.total_dist_up_to = 0

    def add_road(self, to, dist):
        self.connected_to.append((to, dist))

    def get_roads_out(self):
        return self.connected_to

    def best_path_items(self):
        return self.total_items_up_to + self.items


locs = []

N = int(input())
locs = [Location(i, items) for i, items in enumerate(map(int, input().split()))]

M = int(input())
for _ in range(M):
    a, b, d = map(int, input().split())
    a, b = a - 1, b - 1
    locs[a].add_road(b, d)
    locs[b].add_road(a, d)


# Dijkstra's
pq = PriorityQueue()
# dist, (inverse) items up to curr node, curr node index, prev node index
pq.put((0, 0, 0, None))
relaxed = set()
while not pq.empty():
    dist, items_up_to, node, prev_node = pq.get()
    items_up_to = -items_up_to
    if node in relaxed:
        continue

    relaxed.add(node)
    items_up_to = 0
    if prev_node is not None:
        locs[node].best_road_to = prev_node
        items_up_to = locs[prev_node].best_path_items()
        locs[node].total_items_up_to = items_up_to
        locs[node].total_dist_up_to = dist

    for next_node, road_len in locs[node].get_roads_out():
        pq.put((
            dist + road_len,
            -(items_up_to + locs[node].items),
            next_node,
            node))

last_node = locs[-1]
if last_node.best_road_to == None:
    print("impossible")
else:
    print(last_node.total_dist_up_to, last_node.best_path_items())

