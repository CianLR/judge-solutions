class Node:
    def __init__(self, word):
        self.word = word
        self.succ = []

    def is_pre(self, other):
        if len(other.word) - len(self.word) != 1:
            return False
        wi = 0
        diff = False
        for c in other.word:
            if wi >= len(self.word) or c != self.word[wi]:
                if diff:
                    return False
                diff = True
            else:
                wi += 1
        return True


class Solution:
    def make_dag(self, words):
        nodes = []
        for w in words:
            n = Node(w)
            for node in nodes:
                if node.is_pre(n):
                    node.succ.append(n)
                elif n.is_pre(node):
                    n.succ.append(node)
            nodes.append(n)
        return nodes

    def dfs(self, n, memo={}):
        if n in memo:
            return memo[n]
        memo[n] = max(self.dfs(s) for s in n.succ) if len(n.succ) else 0
        memo[n] += 1
        return memo[n]


    def longestStrChain(self, words) -> int:
        dag = self.make_dag(words)
        return max(self.dfs(n) for n in dag)

if __name__ == '__main__':
    tc = [
        ["a","b","ba","bca","bda","bdca"],
        ["xbc","pcxbcf","xb","cxbc","pcxbc"],
        ["abcd","dbqca"]]
    for t in tc:
        print(t, Solution().longestStrChain(t))

