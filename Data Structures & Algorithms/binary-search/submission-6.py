class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bisect(l,r):
            if l>r:
                return -1
            mid=l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return bisect(l,mid-1)
            elif nums[mid]<target:
                return bisect(mid+1,r)

        return bisect(0,len(nums)-1)

        