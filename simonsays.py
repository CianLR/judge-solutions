simon = "Simon says "
N = int(input())
for _ in range(N):
    s = input()
    if s.startswith(simon):
        print(s[len(simon):])
