
def main():
    N, P = (int(x) for x in input().split())
    cars = sorted(int(x) for x in input().split())
    largest_dist = 0
    for n, c in enumerate(cars):
        d = P * (n + 1)
        d0 = cars[0] - (c - d)
        if d0 > largest_dist:
            largest_dist = d0
    print(largest_dist)

if __name__ == '__main__':
    main()

