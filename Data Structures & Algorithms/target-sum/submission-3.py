class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def rec(i,sm):
            if i==len(nums) :        
                return sm==target
            if str(i)+str(sm) in dp:
                return dp[str(i)+str(sm)]

            dp[str(i)+str(sm)]=(rec(i+1,sm+nums[i])+rec(i+1,sm-nums[i]))
            return dp[str(i)+str(sm)]
        return rec(0,0)
