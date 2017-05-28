N = int(input())
busses = sorted(map(int, input().split()))

line = []
i = 0
while i < N:
    j = i
    while j < N - 1 and busses[j] == busses[j+1] - 1:
        j += 1

    if i < j - 1:
        line.append(str(busses[i]) + '-' + str(busses[j]))
        i = j + 1
    else:
        line.append(str(busses[i]))
        i += 1

print(' '.join(line))
