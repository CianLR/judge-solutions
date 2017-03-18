from heapq import nsmallest, nlargest

N, *times = map(int, input().split())

def cross_cost(wait):
    if len(wait) == 1:
        return wait[0]
    elif len(wait) == 2:
        return max(wait)
    elif len(wait) == 3:
        return sum(wait)

    a, b = wait[:2]
    x, y = wait[-2:]

    double_fer_cost = (2 * b) + a + y
    single_fer_cost = x + y + (2 * a)

    rest_cost = cross_cost(wait[:-2])

    return min(double_fer_cost, single_fer_cost) + rest_cost

print(cross_cost(sorted(times)))
