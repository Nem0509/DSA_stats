import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        rs=[True]*n
        rs[0]=rs[1]=False

        for i in range(2,math.isqrt(n)+1):
            if rs[i]:
                for j in range(2*i,n,i):
                    rs[j]=False
        return sum(rs)
            