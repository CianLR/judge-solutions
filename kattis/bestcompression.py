N, b = map(int, input().split())

print("yes" if N < 2**(b + 1) else "no")
