import sys
from collections import defaultdict

class Node:
    def __init__(self):
        self.name = None
        self.children = []
        self.in_edges = 0

class Stats:
    def __init__(self):
        self.visits = 0
        self.neither_paths = 0
        self.fft_only_paths = 0
        self.dac_only_paths = 0
        self.both_paths = 0
    
    def add_paths(self, other):
        if other is None:
            return
        self.neither_paths += other.neither_paths
        self.fft_only_paths += other.fft_only_paths
        self.dac_only_paths += other.dac_only_paths
        self.both_paths += other.both_paths
    
    def __repr__(self):
        return f"Stats(visits={self.visits}, neither_paths={self.neither_paths}, fft_only_paths={self.fft_only_paths}, dac_only_paths={self.dac_only_paths}, both_paths={self.both_paths})"


def dfs(node):
    if node.name == "out":
        return 1
    paths = 0
    for child in node.children:
        paths += dfs(child)
    return paths

def part1(nodes):
    return dfs(nodes["you"])

def dfs_visits(node, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return
    visited.add(node)
    for child in node.children:
        dfs_visits(child, visited)
    return visited


def dfs_stats(node, stats=None, prev_stats=None):
    if stats is None:
        assert node.in_edges == 0
        stats = defaultdict(Stats)
        stats[node].neither_paths = 1

    nstats = stats[node]
    nstats.visits += 1
    if node.name == "fft":
        nstats.fft_only_paths += prev_stats.neither_paths
        nstats.both_paths += prev_stats.dac_only_paths
        assert prev_stats.fft_only_paths == 0
        assert prev_stats.both_paths == 0
    elif node.name == "dac":
        nstats.dac_only_paths += prev_stats.neither_paths
        nstats.both_paths += prev_stats.fft_only_paths
        assert prev_stats.dac_only_paths == 0
        assert prev_stats.both_paths == 0
    else:
        nstats.add_paths(prev_stats)

    if nstats.visits < node.in_edges:
        return

    for child in node.children:
        dfs_stats(child, stats, nstats)
    return stats


def part2(nodes):
    # Trim the graph to remove edges that can't be taken
    # Apparently not needed for this input
    visited = dfs_visits(nodes["svr"])
    for node in nodes.values():
        if node in visited:
            continue
        for ch in node.children:
            ch.in_edges -= 1
    # Gather stats about all the paths
    stats = dfs_stats(nodes["svr"])
    return stats[nodes["out"]].both_paths


def preprocess(lines):
    nodes = defaultdict(Node)
    for line in lines:
        name, *children = line.split()
        name = name[:-1]
        nodes[name].children = [nodes[ch] for ch in children]
        for ch in children:
            nodes[ch].in_edges += 1
    for name, node in nodes.items():
        node.name = name
    return nodes


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <input_file>")
        sys.exit(1)
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()
    lines = preprocess(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
