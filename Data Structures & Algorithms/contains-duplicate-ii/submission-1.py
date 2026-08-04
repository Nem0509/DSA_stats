class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1,i+1+k):
                if j>=len(nums):
                    break
                if nums[i]==nums[j]:
                    return True
        return False