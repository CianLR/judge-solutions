T = int(input())
for _ in range(T):
    records = list(map(int, input().split()))[:-1]
    imports = 0
    for i in range(1, len(records)):
        imports += max(0, records[i] - (records[i - 1] * 2))
    print(imports)    
