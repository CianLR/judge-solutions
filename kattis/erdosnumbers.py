import sys

ERDOS = 'PAUL_ERDOS'

class Node:
    def __init__(self, name):
        self.name = name
        self.co_auth = []

    def add_author(self, auth):
        self.co_auth.append(auth)

def get_dists(nodes):
    q = [ERDOS]
    dists = {ERDOS: 0}
    while q:
        curr, *q = q
        for nxt in nodes[curr].co_auth:
            if nxt in dists:
                continue
            dists[nxt] = dists[curr] + 1
            q.append(nxt)
    return dists

def main():
    authors = {}
    to_list = []
    for i, line in enumerate(sys.stdin.readlines()):
        auth, *co = line.split()
        to_list.append(auth)
        if auth not in authors:
            authors[auth] = Node(auth)
        for c in co:
            if c not in authors:
                authors[c] = Node(c)
            authors[auth].add_author(c)
            authors[c].add_author(auth)
    erdos_nums = get_dists(authors)
    for a in to_list:
        if a in erdos_nums:
            print(a, erdos_nums[a])
        else:
            print(a, "no-connection")

if __name__ == '__main__':
    main()

