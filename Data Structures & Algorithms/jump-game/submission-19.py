class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        p=len(nums)-2
        while p>=0:
            goal=len(nums)-1-p
            if nums[p]<goal:
                j=nums[p]
                for a in range(1,j+1):
                    if nums[p+a]:
                        nums[p]=True
                        break
                if type(nums[p]) is int:
                    nums[p]=False
            if type(nums[p]) is int:
                nums[p]=True
            p-=1
        return nums[0]
