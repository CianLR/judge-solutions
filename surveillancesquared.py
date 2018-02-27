import sys
from collections import namedtuple

Camera = namedtuple("Camera", ["point", "view"])

def magnitude(a):
    return ((a * a.conjugate()) ** 0.5).real

def get_unit(a):
    return a / magnitude(a)

FORTY_FIVE = get_unit(1 + 1j)
EPS        = 1e-9

def can_see(a, b):
    c_point = b.point - a.point
    c_rotated = c_point * (a.view * FORTY_FIVE.conjugate()).conjugate()
    return c_rotated.real > -EPS and c_rotated.imag > -EPS 

def main():
    lines = [l.strip() for l in sys.stdin.readlines()]
    l = 0
    while l < len(lines):
        N = int(lines[l])
        l += 1
        cameras = []
        for _ in range(N):
            x, y, a, b = map(int, lines[l].split())
            cameras.append(Camera(complex(x, y), complex(a, b)))
            l += 1
        
        sees = [0] * N
        for i in range(N):
            for j in range(i + 1, N):
                if can_see(cameras[i], cameras[j]):
                    sees[i] += 1
                if can_see(cameras[j], cameras[i]):
                    sees[j] += 1
        
        for s in sees:
            print(s)

        if l < len(lines):
            print()

if __name__ == '__main__':
    main()

