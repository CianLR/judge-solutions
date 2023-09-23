class Solution:
    def cycle_stop(self, start, gas, cost, verbose=False):
      cur = start
      cgas = gas[start]
      first = True
      while first or cur != start:
        first = False
        if verbose: print(cur, cgas, cost[cur])
        cgas -= cost[cur]
        cur = (cur + 1) % len(gas)
        if cgas < 0:
          return cur
        cgas += gas[cur]
      return -1


    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
      start = 0
      stop = 0
      for start in range(len(gas)):
        if start != stop:
          continue
        stop = self.cycle_stop(start, gas, cost)
        if stop == -1:
          # self.cycle_stop(start, gas, cost, True)
          return start
      return -1
        
        
