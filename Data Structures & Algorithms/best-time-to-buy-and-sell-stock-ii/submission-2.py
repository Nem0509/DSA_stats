class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def rec(n:int, bought:bool):
            if n==len(prices):
                return 0
            if (n,bought) in dp:
                return dp[(n,bought)]
            if bought:
                dp[(n,bought)]= max(rec(n+1,False)+prices[n],rec(n+1,True))
                return max(rec(n+1,False)+prices[n],rec(n+1,True))
            else:
                dp[(n,bought)]=max(rec(n+1,False),rec(n+1,True)-prices[n])
                return max(rec(n+1,False),rec(n+1,True)-prices[n])
        return rec(0,False)
            