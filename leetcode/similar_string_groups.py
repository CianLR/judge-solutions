class Node:
    def __init__(self, word):
        self.word = word
        self.adj = []

    def similar(self, other):
        diffs = 0
        for a, b in zip(self.word, other.word):
            if a != b:
                diffs += 1
            if diffs > 2:
                return False
        return diffs == 2


class Solution:
    def build_dag(self, words):
        nodes = []
        for w in words:
            n = Node(w)
            for node in nodes:
                if n.similar(node):
                    n.adj.append(node)
                    node.adj.append(n)
            nodes.append(n)
        return nodes

    def dfs(self, n, seen):
        if n in seen:
            return
        seen.add(n)
        for a in n.adj:
            self.dfs(a, seen)

    def flood_fill(self, nodes):
        seen = set()
        groups = 0
        for n in nodes:
            if n in seen:
                continue
            groups += 1
            group = set()
            self.dfs(n, group)
            seen |= group
        return groups


    def numSimilarGroups(self, strs) -> int:
        nodes = self.build_dag(set(strs))
        return self.flood_fill(nodes)

if __name__ == '__main__':
    tc = [
        ["tars","rats","arts","star"],
        ["omv","ovm"]]
    for t in tc:
        print(t, Solution().numSimilarGroups(t))
