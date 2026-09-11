class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        c = None
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] > nums[l] and nums[m] > nums[r]:
                l = m
            elif nums[m] < nums[l] and nums[m] < nums[r]:
                r = m
            elif nums[m] == nums[l]:
                c = r
                break
            else:
                c = 0
                break
        print(c)
        l1, r1 = 0, c-1
        while l1 <= r1:
            m1 = (l1 + r1) // 2
            if target == nums[m1]:
                return m1
            elif nums[m1] < target:
                l1 = m1 + 1
            else:
                r1 = m1 - 1

        l2, r2 = c, len(nums) - 1
        while l2 <= r2:
            m2 = (l2 + r2) // 2
            if target == nums[m2]:
                return m2
            elif nums[m2] < target:
                l2 = m2 + 1
            else:
                r2 = m2 - 1
        
        return -1
