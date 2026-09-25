class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        for i,c in enumerate(s):
            dic[c]=i
        print(dic)
        ans=[]
        l=r=0
        cut=-1
        while l<len(s):
            cut=max(cut,dic[s[l]])
            if l==cut:
                ans.append(l-r+1)
                l=r=l+1
                continue
            l+=1
        return ans