class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker=set(nums)
        possiblestart=[]
        for i in nums:
            if i-1 not in checker:
                possiblestart.append(i)
        print(possiblestart)
        ans=0
        for c in possiblestart:
            cnt=1
            print(c)
            while c+1 in checker:
                cnt+=1
                c+=1
            print(cnt)
            ans=max(ans,cnt)
        return ans
