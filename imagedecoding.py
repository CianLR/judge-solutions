
def swap_char(char):
    return '#' if char == '.' else '.'

N = int(input())
while N:
    line_lens = set()
    for _ in range(N):
        char, *runs = input().split()
        runs = [int(x) for x in runs]
        line_lens.add(sum(runs))
        for r in runs:
            print(char * r, end='')
            char = swap_char(char)
        print()
    if len(line_lens) != 1:
        print("Error decoding image")

    N = int(input())
    if N != 0:
        print()

