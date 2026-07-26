class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=1,1
        while j<len(nums):
            if nums[j]==nums[i-1]:
                j+=1
            else:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
                i+=1
        return i
