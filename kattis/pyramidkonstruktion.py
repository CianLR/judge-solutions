
H, N, M = [int(x) for x in input().split()]

needed = 1 + (4* ((H - 1) * H) // 2)
needed -= N
needed -= M * 2

big = 0
small = 0
if needed < 0:
	if N < 1:
		small = 1
else:
	big = needed // 2
	small = needed % 2

print(small, big)
