from collections import defaultdict

N, code, guess = input().split()

code_unmatch_count = defaultdict(int)
guess_unmatch_count = defaultdict(int)

r = 0
for c, g in zip(code, guess):
    if c == g:
        r += 1
    else:
        code_unmatch_count[c] += 1
        guess_unmatch_count[g] += 1

s = 0
for ug in guess_unmatch_count:
    if ug in code_unmatch_count:
        s += min(code_unmatch_count[ug], guess_unmatch_count[ug])

print(r, s)


