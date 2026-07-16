import math
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        shits=set(nums)
        smallshit=math.inf
        bigshit=0
        for i in nums:
            if i>0:
                smallshit=min(smallshit,i)
                bigshit=max(bigshit,i)
        if smallshit==math.inf:
            return 1
        for k in range(1,smallshit):
            if k not in shits:
                return k
        for l in range(smallshit+1,bigshit):
            if l not in shits:
                return l
        return bigshit+1
