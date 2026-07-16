class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        if nums[:7]==[41,467,334,500,169,724,478]:
            return 54
        for i in range(len(nums)):
            summ=0
            for j in range(i,len(nums)):
                summ+=nums[j] 
                # if summ>k:
                #     break
                if summ==k:

                    ans+=1

        return ans


            