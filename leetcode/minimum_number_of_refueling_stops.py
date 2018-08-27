import heapq

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        stations = [(0, 0)] + stations + [[target, 0]]
        best = [{} for _ in range(len(stations) + 1)]
        # (stops, next_station, inv_fuel)
        pq = [(0, 1, -startFuel)]
        while pq:
            stp, stat, fuel = heapq.heappop(pq)
            fuel = -fuel
            if stp in best[stat] and best[stat][stp] > fuel:
                continue
            if stat == len(stations):
                #print stp, stat, fuel, stops
                return stp
            
            dist_to_next = stations[stat][0] - stations[stat - 1][0]
            if fuel < dist_to_next:
                continue
            fuel -= dist_to_next
            if stp not in best[stat + 1] or best[stat + 1][stp] < fuel:
                heapq.heappush(pq, (stp, stat + 1, -fuel))
                best[stat + 1][stp] = fuel
            fuel += stations[stat][1]
            stp += 1
            if stp not in best[stat + 1] or best[stat + 1][stp] < fuel:
                heapq.heappush(pq, (stp, stat + 1, -fuel))
                best[stat + 1][stp] = fuel
        return -1
