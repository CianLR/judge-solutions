from collections import defaultdict

num_wrong_attempts = defaultdict(lambda: 0)
correct_problems = {}

l = input()
while l != '-1':
    time, prob, res = l.split()
    time = int(time)
    res = res == 'right'

    if res:
        correct_problems[prob] = time
    else:
        num_wrong_attempts[prob] += 1

    l = input()

total_time = 0
for p in correct_problems:
    total_time += correct_problems[p] + (num_wrong_attempts[p] * 20)

print(len(correct_problems), total_time)
