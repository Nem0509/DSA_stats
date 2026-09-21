class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #[5,9,3,2,1,0,2,3,3,1,0,0]
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
        print(nums)
        return nums[0]
