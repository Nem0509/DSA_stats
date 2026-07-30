class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out=[]
        nums.sort()
        for n in range(len(nums)):
            if nums[n]>0:
                break
            if n>0 and nums[n]==nums[n-1]:
                continue
            
            target=-1*nums[n]
            i,j=n+1,len(nums)-1
            while i<j:
                if nums[i]+nums[j]==target:
                    out.append([nums[n],nums[i],nums[j]])
                    while i<j and nums[i]==nums[i+1]:
                        i+=1
                    while i<j and nums[j]==nums[j-1]:
                        j-=1
                    i+=1
                    j-=1
                elif nums[i]+nums[j]>target:
                    j-=1
                else:
                    i+=1
        return out