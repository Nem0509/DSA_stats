class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lent=[]
        for i in strs:
            lent.append(str(len(i)))
        encoded=",".join(lent)+"#"+"".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        if s=="":
            return []
        hsh=s.index("#")
        lntstr=s[:hsh]
        strstr=s[hsh+1:]
        lntlist=lntstr.split(",")
        
        decoded=[]
        start=0
        for n in lntlist:
            decoded.append(strstr[start:start+int(n)])
            start+=int(n)
        return decoded
        