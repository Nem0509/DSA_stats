class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def rec(i,buy):
            if i >=len(prices):
                return 0
            if str(i)+str(buy) in dp:
                return dp[str(i)+str(buy)]
            if buy:
                dp[str(i)+str(buy)]=max(prices[i]+rec(i+2,False),rec(i+1,True))
                return dp[str(i)+str(buy)]
            else:
                dp[str(i)+str(buy)]=max(-prices[i]+rec(i+1,True),rec(i+1,False))
                return dp[str(i)+str(buy)]

        return rec(0,False)
