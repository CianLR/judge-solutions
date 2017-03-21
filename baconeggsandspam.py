from collections import defaultdict

N = int(input())
while N:
    menu = defaultdict(set)
    for _ in range(N):
        person, *items = input().split()
        for item in items:
            menu[item].add(person)

    for item in sorted(menu):
        print(item, *sorted(menu[item]))
    print()

    N = int(input())
