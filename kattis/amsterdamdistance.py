from math import pi

def alt_dist(N, M, R, ss, sr, es, er):
    ring_width = R / N
    return (sr * ring_width) + (er * ring_width)

def dist(N, M, R, ss, sr, es, er):
    ring_width = R / N
    d = abs(sr - er) * ring_width
    lo_ring_rad = min(sr, er) * ring_width
    ring_seg = (pi * lo_ring_rad) / M
    d += (ring_seg * abs(ss - es))
    return min(d, alt_dist(N, M, R, ss, sr, es, er))

def main():
    M, N, R = input().split()
    ss, sr, es, er = (int(x) for x in input().split())
    print(dist(int(N), int(M), float(R), ss, sr, es, er))

if __name__ == '__main__':
    main()

