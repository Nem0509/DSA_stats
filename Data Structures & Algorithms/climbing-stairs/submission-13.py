class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        def rec(i):
            if i>n:
                return 0
            if i==n:
                return 1
            if dp[i]:
                return dp[i]
            dp[i]=rec(i+1)+rec(i+2)
            return dp[i]
        return rec(0)

            