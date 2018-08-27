from collections import defaultdict

N = int(input())
pipe_to_parent = {}
for _ in range(N - 1):
    A, B, X, T = map(int, input().split())
    pipe_to_parent[B] = (A, X / 100, T == 1)
L = [int(x) for x in input().split()]

max_input = 0
for i, req in enumerate(L):
    if req == -1:
        continue
    # print("Starting at", i + 1, "need", req)
    curr = i + 1
    while curr != 1:
        curr, perc, sup = pipe_to_parent[curr]
        if sup:
            req **= 0.5
        req /= perc
        # print("    At", curr, "need", req)
    max_input = max(max_input, req)
print(max_input)
