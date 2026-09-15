class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        c=32
        while c:
            c-=1
            if n&1:
                ans=(ans|1)<<1
            else:
                ans=ans<<1
            n=n>>1
        print(bin(ans)[2:])
        return ans//2


