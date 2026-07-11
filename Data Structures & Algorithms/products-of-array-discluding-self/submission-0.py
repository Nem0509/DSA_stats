class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        zerocount=0
        zeroindex=0
        for i in range(0,len(nums)):
            if nums[i]==0:
                zerocount+=1
                if zerocount>1:
                    return [0]*len(nums)
                zeroindex=i
            else:
                p*=nums[i]
        r=[]
        print(p)
        print(zerocount)
        print(zeroindex)
        if zerocount:
            r=[0]*len(nums)
            r[zeroindex]=p
            return r
        else:
            r=[int(p/nums[i]) for i in range(0,len(nums))]
            return r

