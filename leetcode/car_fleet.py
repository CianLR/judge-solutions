EPS = 1e-6

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # s1 * t = d + (s2 * t)
        # s1 = (d / t) + s2
        # 1 / (s1 - s2) = t / d
        # d / (s1 - s2) = t
        cars = sorted(zip(position, speed), key=lambda a: (a[0], -a[1]))
        new_cars = []
        changed = True
        while changed:
            changed = False
            for i in xrange(len(cars)):
                if i + 1 == len(cars) or cars[i + 1][1] >= cars[i][1]:
                    new_cars.append(cars[i])
                    continue
                a, b = cars[i], cars[i + 1]
                time = float(b[0] - a[0]) / (a[1] - b[1])
                intersect = (time * a[1]) + a[0]
                if intersect <= target + EPS:
                    changed = True
                else:
                    new_cars.append(a)
            cars, new_cars = new_cars, []
        return len(cars)
        
        
