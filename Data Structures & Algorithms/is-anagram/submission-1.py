class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts={}
        dictt={}
        for i in range(len(s)):
            dicts[s[i]]=dicts.get(s[i],0)+1
        for i in range(len(t)):
            dictt[t[i]]=dictt.get(t[i],0)+1
        return dicts==dictt