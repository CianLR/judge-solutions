d = {l: i for l, i in zip('ABC', sorted(map(int, input().split())))}
print(' '.join([str(d[c]) for c in input()]))
