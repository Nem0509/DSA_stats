class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp={}
        def rec(i,ofst):

            if i>=len(nums):
                return ofst==0
            if (i,ofst) in dp:
                return dp[(i,ofst)]

            dp[(i,ofst)] = rec(i+1,ofst+nums[i]) or rec(i+1,ofst-nums[i])
            return dp[(i,ofst)]
        return rec(0,0)