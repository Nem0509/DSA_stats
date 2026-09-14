class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        for i in range(32):
            print(bin(1<<i)[2:],bin(n)[2:])
            if (1<<i)&n:
                ans+=1
        return ans