class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i,j=0,len(nums)-1
        ans=0
        while i<j:
            ans=max(ans,min(nums[i],nums[j])*(j-i))
            if nums[i]>nums[j]:
                j-=1
            else:
                i+=1
        return ans