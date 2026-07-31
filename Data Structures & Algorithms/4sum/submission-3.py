class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        r=set()
        for i in range(0,len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                    
                s=target-nums[i]-nums[j]
                a,b=j+1,len(nums)-1
                while a<b:
                    if nums[a]+nums[b]==s:
                        r.add(tuple(sorted([nums[i],nums[j],nums[a],nums[b]])))
                        a+=1
                        while a<b and nums[a]==nums[a-1]:
                            a+=1
                        while b>a and nums[b]==nums[b-1]:
                            b-=1
                    elif nums[a]+nums[b]>s:
                        b-=1
                    elif nums[a]+nums[b]<s:
                        a+=1
        return [list(x) for x in r]
        
                    



                        