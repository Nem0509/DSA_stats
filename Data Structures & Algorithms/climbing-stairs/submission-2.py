class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n        
        
        dp=[0]*n
        dp[n-1]=1
        dp[n-2]=2
        at=n-3
        while at>=0:
            dp[at]=dp[at+1]+dp[at+2]
            at-=1
        return dp[0]
