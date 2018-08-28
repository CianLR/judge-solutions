class Solution:
    def minCostClimbingStairs(self, cost):
        cost_sum = cost + [0]
        for i in xrange(2, len(cost_sum)):
            cost_sum[i] += min(cost_sum[i - 1], cost_sum[i - 2])
        return cost_sum[-1]

