T = int(input())
for _ in range(T):
    stops = int(input())
    pas = 0
    for _ in range(stops):
        pas = (pas * 2) + 1
    print(pas)