class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas)==1 and gas[0]>=cost[0]:
            return 0
        
        fuel=0
        for i in range(len(gas)):
            gas[i]-=cost[i]
        [-1,3,-4,2]
        for i in range(len(gas)):
            if gas[i]>0:
                fuel=0

                for j in range(len(gas)+1):
                    x=(i+j)%len(gas)
                    
                    fuel+=gas[x]

                    if fuel<0:
                        break
                if fuel>=0:
                    return i    
        return -1