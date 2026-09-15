class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(0,len(nums)):
            ans^=i
            ans^=nums[i]
        ans^=len(nums)
        return ans