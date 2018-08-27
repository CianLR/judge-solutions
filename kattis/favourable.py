
T = int(input())
for _ in range(T):
    S = int(input())
    # sec_num: (True, good_end)
    # sec_num: (False, [choice_a, choice_b, choice_c])
    sections = {}
    for _ in range(S):
        sec, *end_or_choice = input().split()
        if len(end_or_choice) == 3:
            sections[sec] = (False, end_or_choice)
        else:
            sections[sec] = (True, end_or_choice[0] == 'favourably')

    _memo = {s_num: int(sec[1]) for s_num, sec in sections.items() if sec[0]}
    def dfs(s_num):
        if s_num in _memo:
            return _memo[s_num]

        sec = sections[s_num]
        if sec[0]:
            return int(sec[1])

        good_ends = 0
        for s in sec[1]:
            good_ends += dfs(s)
        _memo[s_num] = good_ends
        return good_ends

    print(dfs('1'))

