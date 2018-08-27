T = int(input())
for _ in range(T):
    N = int(input())
    votes = [int(input()) for _ in range(N)]
    tot_votes = sum(votes)
    largest = max(votes)
    if votes.count(largest) > 1:
        print('no winner')
    elif largest > tot_votes / 2:
        print('majority winner', votes.index(largest) + 1)
    else:
        print('minority winner', votes.index(largest) + 1)
