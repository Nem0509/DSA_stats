class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for x in nums:
            ans+=[arr+[x] for arr in ans]
        return ans

