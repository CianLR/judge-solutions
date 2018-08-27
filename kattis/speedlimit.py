N = int(input())
while N != -1:
    curr_time = 0
    total_dist = 0
    for _ in range(N):
        speed, time = map(int, input().split())
        total_dist += speed * (time - curr_time)
        curr_time = time

    print(total_dist, 'miles')

    N = int(input())