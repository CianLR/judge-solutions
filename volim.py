K = int(input())
N = int(input())
MAX_TIME = 210

current_holder = K - 1
current_time = 0
for _ in range(N):
    t, res = input().split()
    t = int(t)

    current_time += t
    if current_time > MAX_TIME:
        print(current_holder + 1)
        break

    if res == 'T':
        current_holder = (current_holder + 1) % 8    
