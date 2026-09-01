class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        
        tdic,window={},{}
        for x in t:
            tdic[x]=tdic.get(x,0)+1

        have,need=0,len(tdic)
        minlen=float("inf")
        minind=[-1,-1]

        l=0
        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1
            if s[r] in tdic and window[s[r]]==tdic[s[r]]:
                have+=1
            
            while have==need:
                if (r-l+1)<minlen:
                    minlen=r-l+1
                    minind=[l,r]
                
                if s[l] in tdic and window[s[l]]<=tdic[s[l]]:
                    have-=1    
                window[s[l]]-=1
                l+=1
        l,r=minind
        if minlen!=float("inf"):
            return s[l:r+1]
        else:
            return ""

                
        # if len(s)<len(t):
        #     return ""
        # elif s.isupper() != t.isupper():
        #     return ""

        # us=s.upper()
        # ut=t.upper()
        # sl,tl=[0]*26,[0]*26

        # for i in us:
        #     index=ord(i)-ord("A")
        #     sl[index]+=1
        # for i in ut:
        #     index=ord(i)-ord("A")
        #     tl[index]+=1
        
        # if len(s)==len(t) and sl==tl:
        #     return s
        # elif len(s)==len(t) and sl!=tl:
        #     return ""

        # l,r=0,len(us)-1

        # while l<len(us) and sl[ord(us[l])-ord("A")]>tl[ord(us[l])-ord("A")]:
        #     sl[ord(us[l])-ord("A")]-=1
        #     l+=1
        # while r>=0 and sl[ord(us[r])-ord("A")]>tl[ord(us[r])-ord("A")]:
        #     sl[ord(us[r])-ord("A")]-=1
        #     r-=1

        # if s.isupper():
        #     return s[l:r+1]
        # else:
        #     return s[l:r+1].lower()