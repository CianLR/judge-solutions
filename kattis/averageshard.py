T = int(input())
for _ in range(T):
    input()
    C, E = map(int, input().split())
    students = []
    while len(students) < C + E:
        students.extend([int(x) for x in input().split()])
    cs, econ = sorted(students[:C]), sorted(students[C:])
    cs_avg = sum(cs) / C
    econ_avg = sum(econ) / E

    ans = 0
    for s in cs:
        if s >= cs_avg:
            break
        elif s <= econ_avg:
            continue
        ans += 1

    print(ans)
