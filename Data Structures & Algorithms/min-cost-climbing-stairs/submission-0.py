class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-3,-1,-1):
            cost[i]+=min(cost[i+1],cost[i+2])

        if len(cost)>1:
            return min(cost[0],cost[1])
        else:
            return 0