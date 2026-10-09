class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=len(s)
        for i in range(1,len(s)-1):
            a=i-1
            b=i+1
            while a>=0 and b<len(s) and s[a]==s[b]:
                ans+=1
                a-=1
                b+=1
        
        for i in range(0,len(s)):
            a=i
            b=i+1
            while a>=0 and b<len(s) and s[a]==s[b]:
                ans+=1
                a-=1
                b+=1

        return ans

