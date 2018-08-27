from collections import defaultdict

def main():
    N = int(input())
    arrows = [0] * 1000000
    shot = 0
    for h in (int(x) for x in input().split()):
        if not arrows[h]:
            shot += 1
            if h - 1 >= 0:
                arrows[h - 1] += 1
        else:
            arrows[h] -= 1
            if h - 1 >= 0:
                arrows[h - 1] += 1
    print(shot)

if __name__ == '__main__':
    main()

