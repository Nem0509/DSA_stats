class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,0,-1):
            nums[i]=nums[i]-nums[i-1]
        ans=0
        s=0
        print(nums)
        for j in range(1,len(nums)):
            s+=nums[j]
            ans=max(s,ans)
            if s<0:
                s=0
            
        return ans
