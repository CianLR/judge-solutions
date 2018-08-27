
N = int(raw_input())
for _ in range(N):
    num = list(raw_input())
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            num[i] = str(int(num[i]) - 1)
            break
    print int(''.join(num))

