from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic=Counter(list(s))
        ans=[]
        nm=0
        tar={}
        l=0
        r=0
        while l<len(s):
            if s[l] not in tar:
                tar[s[l]]=1
                nm+=1
            else:
                tar[s[l]]+=1
            if tar[s[l]]==dic[s[l]]:
                nm-=1
            if nm==0:
                ans.append(l-r+1)
                l=r=l+1
                continue
            l+=1
        return ans

                
            
