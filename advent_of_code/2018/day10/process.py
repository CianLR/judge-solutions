import sys

class Point:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

def main():
    points = []
    for line in sys.stdin.readlines():
        p1, p2 = line.strip()[len('position=<'):-1].split('> velocity=<')
        points.append(Point(
            tuple(map(int, p1.lstrip().split(', '))),
            tuple(map(int, p2.lstrip().split(', ')))
        ))
    for p in points:
        print "  stars.add(new Star({}, {}, {}, {}));".format(*(p.pos + p.vel))

if __name__ == '__main__':
    main()

