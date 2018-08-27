from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = {0}
        stack = deque([0])
        while stack:
            u = stack.pop()
            for v in rooms[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
        return len(visited) == len(rooms)
        
