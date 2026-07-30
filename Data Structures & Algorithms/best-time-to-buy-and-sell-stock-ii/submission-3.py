class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nbuy=0
        nsell=0
        tbuy=0
        tsell=0
        for i in range(len(prices)-1,-1,-1):
            tbuy=max(nbuy,-prices[i]+nsell)
            tsell=max(tsell,prices[i]+nbuy)
            nbuy=tbuy
            nsell=tsell
        return tbuy
            