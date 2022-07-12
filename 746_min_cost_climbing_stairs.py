# 746. Min Cost Climbing Stairs

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step_count = len(cost)
        
        for step in range(step_count - 3, -1, -1):
            cost[step] = cost[step] + min(cost[step + 1], cost[step + 2])

        return min(cost[0], cost[1])
    