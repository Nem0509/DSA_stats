class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        res.append(0)
        for x in range(1,n+1):
            cnt=0
            while x:
                cnt+=1
                x&=(x-1)
            res.append(cnt)
        return res