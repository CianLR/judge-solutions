w, l = map(int, input().split())

while w or l:
    N = int(input())
    actual = (0, 0)
    thinks = (0, 0)
    for _ in range(N):
        dr, dist = input().split()
        dist = int(dist)
        if dr == 'u':
            thinks = (thinks[0], thinks[1] + dist)
            actual = (
                actual[0],
                min(max(actual[1] + dist, 0), l - 1)
            )
        elif dr == 'd':
            thinks = (thinks[0], thinks[1] - dist)
            actual = (
                actual[0],
                min(max(actual[1] - dist, 0), l - 1)
            )
        elif dr == 'l':
            thinks = (thinks[0] - dist, thinks[1])
            actual = (
                min(max(actual[0] - dist, 0), w - 1),
                actual[1]
            )
        else:
            thinks = (thinks[0] + dist, thinks[1])
            actual = (
                min(max(actual[0] + dist, 0), w - 1),
                actual[1]
            )
    print("Robot thinks", *thinks)
    print("Actually at", *actual)
    print()

    w, l = map(int, input().split())

