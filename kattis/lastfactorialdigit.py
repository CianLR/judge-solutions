
for _ in range(int(input())):
    print((lambda x: [0, 1, 2, 6, 4][x] if x < 5 else 0)(int(input())))

