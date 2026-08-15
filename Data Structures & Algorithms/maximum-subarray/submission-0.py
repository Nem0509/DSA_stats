class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=0
        insum=0
        for i in nums:
            insum+=i
            ans=max(ans,insum)
            if insum<0:
                insum=0
        if ans==0 and 0 not in nums:
            return -1

        return ans
