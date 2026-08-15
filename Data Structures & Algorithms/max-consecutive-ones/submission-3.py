class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        cnt=0

        for i in range(0,len(nums)):
            if nums[i]==1:
                cnt+=1
                ans=max(ans,cnt)
            else:
                cnt=0
        return ans
            
