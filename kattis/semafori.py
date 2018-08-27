N, L = map(int, input().split())
lights = []

curr_time = 0
curr_pos = 0
for _ in range(N):
    D, R, G = map(int, input().split())
    curr_time += D - curr_pos
    curr_pos = D

    cycle_point = curr_time % (R + G)
    curr_time += max(R - cycle_point, 0)

curr_time += L - curr_pos
print(curr_time)
