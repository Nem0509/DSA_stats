class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(m):
            cnt=0
            for x in piles:
                cnt+=(x+m-1)//m
            return cnt<=h
        
        piles.sort()
        l=1
        r=piles[-1]

        while l<=r:
            m=l+((r-l)>>1)
            if check(m):
                r=m-1
            else:
                l=m+1
        
        return r+1
