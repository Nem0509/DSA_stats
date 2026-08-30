class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans=0
        i=0
        dic={}
        for r in range(len(s)):
            dic[s[r]]=dic.get(s[r],0)+1
            while ((r-i+1)-(max(dic.values())))>k:
                dic[s[i]]=dic[s[i]]-1
                i+=1
            ans=max(ans,r-i+1)
        return ans
