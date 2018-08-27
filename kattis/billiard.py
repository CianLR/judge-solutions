from math import degrees, atan

def main():
    a, b, s, m, n = [int(x) for x in input().split()]
    while a or b or s or m or n:
        angle = degrees(atan((b * n) / (a * m)))
        dist = ((b * n) ** 2 + (a * m) ** 2) ** 0.5
        veloc = dist / s
        print("{:.2f} {:.2f}".format(angle, veloc))
        
        a, b, s, m, n = map(int, input().split())

if __name__ == '__main__':
    main()

