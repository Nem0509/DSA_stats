class Solution:

    def encode(self, strs: List[str]) -> str:
        for s in range(len(strs)):
            strs[s]=str(len(strs[s]))+"#"+strs[s]
        encoded="".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        st=0
        ans=[]
        i=0
        while i<(len(s)):
            if s[i]=="#":
                print(s[st:i])
                cnt=int(s[st:i])
                ans.append(s[i+1:i+1+cnt])
                i=i+cnt+1
                st=i
                if st>len(s):
                    break
            else:
                i+=1
        return ans


