class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=2
        if n==1:
            return a
        elif n==2:
            return b
        for i in range(2,n):
            t=a+b
            a=b
            b=t
        return b
        