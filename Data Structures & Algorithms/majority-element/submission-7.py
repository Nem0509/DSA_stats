class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        leader, count=0,0
        for i in nums:
            if count==0:
                leader=i
                count+=1
            elif i==leader:
                count+=1
            elif i!=leader:
                count-=1
        return leader