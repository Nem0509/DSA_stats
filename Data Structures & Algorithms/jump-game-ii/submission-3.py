class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        for i in range(len(nums)-2,-1,-1):
            goal=len(nums)-1-i
            if nums[i]>=goal:
                nums[i]=1
            else:
                mj=float('inf')
                p=i
                for j in range(1,nums[i]+1):
                    mj=min(mj,nums[p+j])
                nums[i]=mj+1
        return nums[0]