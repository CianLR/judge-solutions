T = int(input())
for _ in range(T):
    D, M = map(int, input().split())
    days = [int(x) for x in input().split()]
    month_starts = []
    for i in range(M):
        month_starts.append(sum(days[:i]))

    FRIDAY = 6
    friday_count = 0
    for abs_day, month_len in zip(month_starts, days):
        if month_len < 13:
            continue
        if (abs_day + 13) % 7 == FRIDAY:
            friday_count += 1
    print(friday_count)
