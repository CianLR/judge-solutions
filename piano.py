import heapq

START = 0
END   = 1

def can_move(N, P, moves, skip_days):
    move_i = 0
    end_times = []
    for day in xrange(1, 101):
        while move_i < len(moves) and moves[move_i][0] <= day:
            heapq.heappush(end_times, moves[move_i][1])
            move_i += 1
        if day % 7 not in skip_days:
            for _ in xrange(P / 2):
                if not end_times:
                    break
                heapq.heappop(end_times)
        if end_times and end_times[0] <= day:
            return False
        if not end_times and move_i == len(moves):
            break
    return True

def move_type(N, P, moves):
    moves = sorted(moves)
    if can_move(N, P, moves, {0, 6}):
        return "fine"
    elif can_move(N, P, moves, set()):
        return "weekend work"
    return "serious trouble"

def main():
    T = int(raw_input())
    for _ in range(T):
        N, P = (int(x) for x in raw_input().split())
        moves = [tuple(int(x) for x in raw_input().split()) for _ in range(N)]
        print move_type(N, P, moves)

if __name__ == '__main__':
    main()

