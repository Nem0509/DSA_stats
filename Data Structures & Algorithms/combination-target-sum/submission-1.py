class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res=[]
        def rec(i,cur,add):
            if i>=len(nums):
                return 
            if add==target:
                res.append(cur.copy())
                return
            elif add>target:
                return
            else:
                cur.append(nums[i])
                rec(i,cur,add+nums[i])
                cur.pop()
                rec(i+1,cur,add)

        rec(0,[],0)
        return res
