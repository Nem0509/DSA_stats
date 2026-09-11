class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<3:
            return min(nums)
        
        l=0
        r=len(nums)-1
        m=0
        while l<=r:
            m= l+((r-l)//2)
            print(m)
            if nums[m]>nums[l] and nums[m]>nums[r]:
                l=m
            elif nums[m]<nums[l] and nums[m]<nums[r]:
                r=m
            elif nums[m]==nums[l]:
                return nums[r]
            else:
                return nums[0] 
        # return nums[l+1]