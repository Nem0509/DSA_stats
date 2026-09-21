class Solution:
    def canJump(self, nums: List[int]) -> bool:
        [5,9,3,2,1,0,2,3,3,1,0,0]
        
        i=0
        while i<len(nums):
            if i==len(nums)-1:
                return True
            if nums[i]==0:
                return False
            if i+1<len(nums) and nums[i+1]==0:
                zc=0
                p=i
                while p+1<len(nums) and nums[p+1]==0:
                    zc+=1
                    p+=1

                if p+1==len(nums):
                    j=zc
                    x=i
                    while x>=0:
                        if nums[x]>=j:
                            break
                        x-=1
                        j+=1
                    if x<0:
                        return False
                    else:
                        return True
                elif p+1<len(nums):
                    j=zc
                    x=i
                    while x>=0:
                        if nums[x]>j:
                            break
                        x-=1
                        j+=1
                    if x<0:
                        return False
                    else:
                        i=p+1
                        continue
            i+=1
        return False
                    
