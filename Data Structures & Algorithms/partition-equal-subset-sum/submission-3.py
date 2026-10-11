class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp={}
        def rec(i,ofst):

            if i>=len(nums):
                return ofst==0
            if str(i)+str(ofst) in dp:
                return dp[str(i)+str(ofst)]

            dp[str(i)+str(ofst)] = rec(i+1,ofst+nums[i]) or rec(i+1,ofst-nums[i])
            return dp[str(i)+str(ofst)]
        return rec(0,0)