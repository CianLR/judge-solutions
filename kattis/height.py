P = int(input())
for _ in range(P):
    K, *heights = map(int, input().split())
    seen_students = []
    steps_back = 0
    for s in heights:
        steps_back += len([i for i in seen_students if i > s])
        seen_students.append(s)
    print(K, steps_back)
