import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans=bisect.bisect_left(nums,target)
        if ans<len(nums) and nums[ans]==target:
            return ans
        else:
            return -1
        