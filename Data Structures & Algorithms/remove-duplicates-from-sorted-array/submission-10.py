class Solution:
    def removeDuplicates(self, nums: List[int]) -> List:
        st=set(nums)
        l=len(st)
        i=0
        while i<l-1:
            if nums[i]==nums[i+1]:
                del nums[i+1]
            else:
                i+=1
        return l