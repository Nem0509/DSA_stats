class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums,default=0)
        
        lst1=nums.copy()
        lst1.pop()
        lst2=nums.copy()
        del lst2[0]

        dp1=[-1]*(len(nums))
        dp2=[-1]*(len(nums))

        def rec1(lst,i):
            if i >=len(lst):
                return 0
            if dp1[i]!=-1:
                return dp1[i]
         
            dp1[i]=max(lst[i]+rec1(lst,i+2),rec1(lst,i+1))
            return dp1[i]

        def rec2(lst,i):
            if i >=len(lst):
                return 0
            if dp2[i]!=-1:
                return dp2[i]
         
            dp2[i]=max(lst[i]+rec2(lst,i+2),rec2(lst,i+1))
            return dp2[i]

        return max(rec1(lst1,0),rec2(lst2,0))
        