from collections import defaultdict

case_no = 1
N = int(input())
while N:
    animals = defaultdict(int)
    for _ in range(N):
        a = input().split()[-1].lower()
        animals[a] += 1

    print("List {}:".format(case_no))
    for a in sorted(animals):
        print(a, '|', animals[a])
    case_no += 1

    N = int(input())
