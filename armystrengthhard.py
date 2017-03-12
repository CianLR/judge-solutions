T = int(input())
for _ in range(T):
    input()
    Ng, Nm = map(int, input().split())
    gz = sorted(map(int, input().split()), reverse=True)
    mg = sorted(map(int, input().split()), reverse=True)
    while gz and mg:
        if gz[-1] < mg[-1]:
            gz.pop()
        else:
            mg.pop()
    if gz:
        print("Godzilla")
    else:
        print("MechaGodzilla")
