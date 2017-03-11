from queue import PriorityQueue

cup_pq = PriorityQueue()
N = int(input())
for _ in range(N):
    a, b = input().split()
    try:
        cup_pq.put((int(b), a))
    except:
        cup_pq.put((int(a)//2, b))

while not cup_pq.empty():
    print(cup_pq.get()[1])
