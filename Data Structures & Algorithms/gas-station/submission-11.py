class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l=0
        r=len(gas)-1
        tank=0
        tank+=gas[r]-cost[r]
        while l<r:
            if tank<0:
                r-=1
                tank+=gas[r]-cost[r]
            elif tank>=0:

                tank+=gas[l]-cost[l]
                l+=1

        return r if tank>=0 else -1