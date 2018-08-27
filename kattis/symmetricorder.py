N = int(input())
set_count = 1
while N != 0:
    name_pairs = [(input(), input()) for _ in range(N//2)][::-1]
    smooth_names = [input()] if N%2 else []

    for top, bot in name_pairs:
        smooth_names = [top] + smooth_names + [bot]

    print("SET", set_count)
    print('\n'.join(smooth_names))

    set_count += 1
    N = int(input())
