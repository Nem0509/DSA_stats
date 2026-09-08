class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = (l+r) // 2

            if target==nums[m]:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r=m-1
        return -1