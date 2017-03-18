C = int(input())
for case in range(1, C + 1):
    N, T = map(int, input().split())
    E = int(input())
    employees = [[] for _ in range(N)]
    for _ in range(E):
        h, p = map(int, input().split())
        employees[h - 1].append(p)
    
    cars = [0]*N
    for i in range(N):
        if i == T - 1:
            continue
        people = sorted(employees[i])
        if sum(people) < len(people):
            cars[i] = -1
            break
        while people:
            *people, largest = people
            people = [] if largest > len(people) else people[largest - 1:] 
            cars[i] += 1

    print("Case #{}: ".format(case), end='')
    if -1 in cars:
        print("IMPOSSIBLE")
    else:
        print(*cars)



