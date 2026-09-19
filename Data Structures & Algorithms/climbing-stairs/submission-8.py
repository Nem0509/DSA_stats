class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[-1],dp[-2]=1,2
        def rec(i):
            if dp[i]:
                return dp[i]
            if i>=n and i==n:
                dp[n]=1
                return
            dp[i]=rec(i+1)+rec(i+2)
            return dp[i]
        rec(1)
        return dp[1]

            