class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums,0,len(nums)-1)
        return nums
    
    def quicksort(self, nums, s, e):
        if e-s<=1:
            if e-s==1 and nums[e]<nums[s]:
                nums[e],nums[s]=nums[s],nums[e]
            return nums
        p=self.partition(nums, s, e)
        self.quicksort(nums,s,p-1)
        self.quicksort(nums,p+1,e)
    
    def partition(self, nums, s, e):
        l=e-s+1
        m=s+(l>>1)

        temp=[[nums[s],s],[nums[m],m],[nums[e],e]]
        temp.sort()
        piv=temp[1][1]
        nums[piv],nums[e]=nums[e],nums[piv]

        i,j=s,e
        while i<j:
            if nums[i]<nums[e]:
                i+=1
            elif nums[i]>=nums[e]:
                j-=1
                nums[i],nums[j]=nums[j],nums[i]
        nums[j],nums[e]=nums[e],nums[j]
        return j



