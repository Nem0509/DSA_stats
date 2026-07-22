class Solution:
    def removeDuplicates(self, nums: List[int]) -> List:
        i,j=1,1
        while j<len(nums):
            if nums[j]==nums[i-1]:
                j+=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
        return i
