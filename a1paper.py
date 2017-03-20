N = int(input())
quants = [0, 0] + list(map(int, input().split()))

def side_len(a_ind, _memo={}):
    if a_ind in _memo:
        pass
    elif a_ind % 2:
        side = 0.8408964152537145 * 2 ** (-(a_ind//2))
        _memo[a_ind] = side
    else:
        side = 2 ** (-3/4) * 2 ** -((a_ind//2) - 1)
        _memo[a_ind] = side
    return _memo[a_ind]

def tape_needed(a_ind, num):
    if a_ind > N:
        # Oh god I'm lazy
        raise Exception("impossible")

    if num <= quants[a_ind]:
        # I have enough paper, no creation needed
        return 0

    needed = num - quants[a_ind]
    next_ind_needed = 2 * needed
    next_ind_tape_req = tape_needed(a_ind + 1, next_ind_needed)
    return (needed * side_len(a_ind + 1)) + next_ind_tape_req

try:
    print(tape_needed(1, 1))
except Exception as e:
    print(e)
