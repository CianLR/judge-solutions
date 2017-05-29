X = int(input())
line = [p for p in input()]

front = 0
second = 1
diff = 0
people_in = 0

def let_in_front():
    global front
    global second
    global diff
    # print("Letting in", line[front], "in first")
    diff += 1 if line[front] == "M" else -1
    front, second = second, second + 1

def let_in_second():
    global front
    global second
    global diff
    # print("Letting in", line[second], "in second")
    diff += 1 if line[second] == "M" else -1
    second += 1

while second < len(line) and abs(diff) <= X:
    if diff > 0:
        if line[front] == 'W':
            let_in_front()
        elif line[second] == 'W':
            let_in_second()
        else:
            let_in_second()
    else:
        if line[front] == 'M':
            let_in_front()
        elif line[second] == 'M':
            let_in_second()
        else:
            let_in_front()
    people_in += 1



if abs(diff) > X:
    print(people_in - 1)
else:
    print(people_in + 1)
