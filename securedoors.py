from collections import defaultdict
N = int(input())
in_building = defaultdict(bool)
for _ in range(N):
    act, person = input().split()
    if act == 'entry':
        if not in_building[person]:
            print(person, 'entered')
        else:
            print(person, 'entered (ANOMALY)')
        in_building[person] = True
    else:
        if in_building[person]:
            print(person, 'exited')
        else:
            print(person, 'exited (ANOMALY)')
        in_building[person] = False
