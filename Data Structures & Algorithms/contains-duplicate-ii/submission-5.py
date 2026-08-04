class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s=set()
        n=0
        if k==0:
            return False
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return True
            if len(s)>k:
                s.remove(nums[n])
                n+=1
        return False
