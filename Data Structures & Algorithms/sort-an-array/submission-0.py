class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for j in range(1,len(nums)):
            a=j
            for i in range(j-1,-1,-1):
                if nums[i]>=nums[a]:
                    nums[i],nums[a]=nums[a],nums[i]
                    a=i
                elif nums[i]<nums[a]:
                    break
        return nums
        


