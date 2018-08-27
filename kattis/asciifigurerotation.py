N = int(input())
while N != 0:
    figure = [input() for _ in range(N)]
    new_height = max(map(len, figure))
    for row in range(new_height):
        out_line = ''
        for col in range(N - 1, -1, -1):
            if row >= len(figure[col]):
                out_line += ' '
                continue
            c = figure[col][row]
            if c == '|':
                c = '-'
            elif c == '-':
                c = '|'
            out_line += c
        print(out_line.rstrip())

    N = int(input())
    if N == 0:
        break
    print()
