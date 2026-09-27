class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res=[]
        nums.sort()
        no=target//min(nums)
        def rec(i,cur,add):
            if i>=len(nums) or len(cur)>no:
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
