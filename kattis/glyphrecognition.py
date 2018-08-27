from math import pi, atan2, tan, sin, cos

def interior_angle(sides):
    return (pi * (sides - 2)) / sides

IA = [0, 0, 0, *map(interior_angle, range(3, 9))]
SEG_ANGLE = [0, 0, 0, *map(lambda s: pi * 2 / s, range(3, 9))]

def circ_rotation(point):
    h = atan2(point.imag, point.real)
    return h if h >= 0 else (pi * 2) + h

def radius(point, sides):
    return (point.imag / tan(IA[sides] / 2)) + point.real

def segment_area(rad, angle):
    return 0.5 * (rad ** 2) * sin(angle)

def poly_area(point, sides):
    rot = circ_rotation(point)
    rotate_back = (rot // SEG_ANGLE[sides]) * SEG_ANGLE[sides]
    rotated_point = point / complex(cos(rotate_back), sin(rotate_back))
    r = radius(rotated_point, sides)
    return sides * segment_area(r, SEG_ANGLE[sides])

def main():
    N = int(input())
    points = [complex(*(int(x) for x in input().split())) for _ in range(N)]
    best_shape = None
    best_score = 0
    for sides in range(3, 9):
        areas = [poly_area(p, sides) for p in points]
        score = min(areas) / max(areas)
        if score > best_score:
            best_score = score
            best_shape = sides
    print(best_shape, best_score)

if __name__ == '__main__':
    main()

