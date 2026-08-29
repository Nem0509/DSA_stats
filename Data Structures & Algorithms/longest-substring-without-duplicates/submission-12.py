class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans=0
        dup=set()
        l=0
        r=0

        while r<len(s):
            if s[r] not in dup:
                dup.add(s[r])
                r+=1
                ans=max(ans,r-l)
            else:
                ans=max(ans,r-l)
                while s[r] in dup:
                    dup.discard(s[l])
                    l+=1
        return ans
            