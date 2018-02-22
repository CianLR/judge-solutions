
def get_best_team(runners):
    best_start = sorted(runners, key=lambda r: r[1])[:4]
    best_rest  = sorted(runners, key=lambda r: r[2])[:4]
    best_time  = (100, None, None, None, None)
    for start_run in best_start:
        team = []
        for rest_run in best_rest:
            if rest_run == start_run:
                continue
            team.append(rest_run)
            if len(team) == 3:
                break
        time = start_run[1] + sum(r[2] for r in team)
        best_time = min(best_time, (time, start_run, *team))
    return best_time

def main():
    N = int(input())
    runners = []
    for _ in range(N):
        name, first, rest = input().split()
        runners.append((name, float(first), float(rest)))
    
    time, *team = get_best_team(runners)
    print(time)
    for t in team:
        print(t[0])

if __name__ == '__main__':
    main()

