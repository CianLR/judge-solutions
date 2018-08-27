N, time_left = map(int, input().split())
tasks = map(int, input().split())
task_done = 0
for task in tasks:
    if task > time_left:
        break
    time_left -= task
    task_done += 1

print(task_done)
