from math import radians, cos

def velocity(v0, d, a):
    return ((v0 ** 2) + (2 * a * d)) ** 0.5

def angle_to_accel(g, theta):
    return g * cos(radians(theta))

def main():
    N, G = raw_input().split()
    N, G = int(N), float(G)
    speeds = []
    for _ in xrange(N):
        D, theta = (int(x) for x in raw_input().split())
        speeds.append(0)
        for i in xrange(len(speeds)):
            speeds[i] = velocity(speeds[i], D, angle_to_accel(G, theta))
    
    for s in speeds:
        print s

if __name__ == '__main__':
    main()

