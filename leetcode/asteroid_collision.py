class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        changed = True
        while changed:
            changed = False
            for i in xrange(len(asteroids) - 2, -1, -1):
                if i + 1 >= len(asteroids):
                    continue
                if asteroids[i] > 0 and asteroids[i + 1] < 0:
                    if abs(asteroids[i]) > abs(asteroids[i + 1]):
                        asteroids[i:i+2] = [asteroids[i]]
                    elif abs(asteroids[i]) < abs(asteroids[i + 1]):
                        asteroids[i:i+2] = [asteroids[i + 1]]
                    else:
                        asteroids[i:i+2] = []
                    changed = True
        return asteroids
        
