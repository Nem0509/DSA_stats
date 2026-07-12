class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        p=0
        for i in range(0,len(prices)-1):
            b=prices[i]
            s=prices[i+1]
            if s-b>=1:
                p+=s-b
        return p


            