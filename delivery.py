
def trip_cost(houses, K):
    dists = [h[0] for h in houses]
    caps = [h[1] for h in houses]
    cost = 0
    last = len(houses) - 1
    while caps and caps[0]:
        van = K
        run_cost = 0
        #print("Cap is at", van)
        for i in xrange(last, -1, -1):
            #print("  At house", i)
            if caps[i] == 0:
                continue
            if not run_cost:
                run_cost = 2 * dists[i]
            if van <= caps[i]:
                #print("  A: Delivering", van, "of", caps[i])
                caps[i] -= van
                last = i
                break
            else:
                #print("  B: Delivering", caps[i], "of", caps[i])
                van -= caps[i]
                caps[i] = 0
        cost += run_cost
    return cost


def main():
    N, K = raw_input().split()
    N, K = int(N), int(K)
    neg, pos = [], []
    for _ in xrange(N):
        dist, cap = raw_input().split()
        dist, cap = int(dist), int(cap)
        if dist < 0:
            neg.append((-dist, cap))
        else:
            pos.append((dist, cap))
    
    cost = trip_cost(sorted(neg), K)
    cost += trip_cost(sorted(pos), K)
    print cost



if __name__ == '__main__':
    main()

