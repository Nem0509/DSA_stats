class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        print(nums)
        i,j=0,len(nums)-1
        ans=0
        while i<=j:
            if nums[j]==limit:
                ans+=1
                j-=1
            elif nums[i]<=limit-nums[j]:
                ans+=1
                j-=1
                i+=1
            else:
                ans+=1
                j-=1
        return ans