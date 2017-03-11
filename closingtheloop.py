from queue import PriorityQueue

N = int(input())
for i in range(1, N + 1):
    S = int(input())
    blue_rope = PriorityQueue()
    red_rope = PriorityQueue()
    for rope in input().split():
        l, col = int(rope[:-1]), rope[-1]
        if col == 'B':
            blue_rope.put(-l)
        else:
            red_rope.put(-l)

    rope_lens = []
    while (not blue_rope.empty()) and (not red_rope.empty()):
        rope_lens.append(-blue_rope.get())
        rope_lens.append(-red_rope.get())

    print("Case #{}: {}".format(
        i, sum(rope_lens) - len(rope_lens)))

