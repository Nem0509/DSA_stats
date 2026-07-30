class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l=len(nums)
        for i in range(l-1,-1,-1):
            if nums[i]<0:
                nums[i]=0
        for i in range(l):
            if 0<abs(nums[i])<l+1 and nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1]=-1*nums[abs(nums[i])-1]
            elif 0<abs(nums[i])<l+1 and nums[abs(nums[i])-1]==0:
                nums[abs(nums[i])-1]=-(l+1)
        print(nums)
        for i in range(l):
            if nums[i]>=0:
                return i+1
        return l+1