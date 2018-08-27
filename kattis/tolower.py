
P, T = map(int, input().split())

solved = 0
for _ in range(P):
    cases = [input() for _ in range(T)]
    solved += all(map(lambda s: s[1:] == s[1:].lower(), cases))
print(solved)

