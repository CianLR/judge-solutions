class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obs = {tuple(o) for o in obstacles}
        loc = (0, 0)
        direc = 0
        maxd = 0
        for c in commands:
            if c == -2:
                direc = (direc - 1) % 4
            elif c == -1:
                direc = (direc + 1) % 4
            else:
                while c:
                    nloc = (loc[0] + DIRS[direc][0], loc[1] + DIRS[direc][1])
                    if nloc in obs:
                        break
                    loc = nloc
                    c -= 1
                if loc[0]**2 + loc[1]**2 > maxd:
                    maxd = loc[0]**2 + loc[1]**2
        return maxd 
        
