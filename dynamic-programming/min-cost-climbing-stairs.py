class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 2:
            return min(cost[0], cost[1])
        total_cost = [0]*len(cost)
        total_cost[-1] = cost[-1]
        total_cost[-2] = cost[-2]
        for i in range(3, len(cost) + 1):
            total_cost[len(cost) - i] = cost[len(cost) - i] + min(total_cost[len(cost) - i + 1], total_cost[len(cost) - i + 2])
        return min(total_cost[0], total_cost[1])
