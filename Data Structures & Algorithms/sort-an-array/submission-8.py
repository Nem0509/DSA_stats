class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums,0,len(nums)-1)
        return nums

    def partition(self, nums,s,e):
        m=s+((e-s)>>1)
        
        dic=[[nums[s],s],[nums[m],m],[nums[e],e]]
        dic.sort(key=lambda x:x[0])
        p=dic[1][1]

        nums[p],nums[e]=nums[e],nums[p]

        i,j=s,e
        while i<j:
            if nums[i]<nums[e]:
                i+=1
            elif nums[i]>=nums[e]:
                nums[i],nums[j-1]=nums[j-1],nums[i]
                j-=1

        nums[e],nums[j]=nums[j],nums[e]
        return j
    
    def quicksort(self,nums,s,e):
        if e-s<=1:
            if e-s==1 and nums[s]>nums[e]:
                nums[e],nums[s]=nums[s],nums[e]
            return nums

        p=self.partition(nums,s,e)
        self.quicksort(nums,s,p-1)
        self.quicksort(nums,p+1,e)
        
        


