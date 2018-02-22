from math import cos, sin, radians, hypot

def walk(point, direction, steps):
    return point + (direction * steps), direction

def turn(point, direction, degrees):
    return point, direction * complex(cos(radians(degrees)),
                                      sin(radians(degrees)))

COMMANDS = {
    'walk': walk,
    'turn': turn,
    'start': turn,
}

def get_end_point(start_x, start_y, instrs):
    point = complex(start_x, start_y)
    direction = 1 + 0j
    for cmd, val in instrs:
        point, direction = COMMANDS[cmd](point, direction, val)
    return point

def complex_dist(a, b):
    c = a - b
    return hypot(c.real, c.imag)

def main():
    N = int(input())
    while N:
        ends = []
        for _ in range(N):
            start_x, start_y, *cmds = input().split()
            ends.append(get_end_point(
                float(start_x),
                float(start_y),
                zip(cmds[::2], map(float, cmds[1::2]))))
        
        average = sum(ends) / len(ends)
        furthest = max(complex_dist(average, x) for x in ends)
        print(average.real, average.imag, furthest)
            
        N = int(input())

if __name__ == '__main__':
    main()

