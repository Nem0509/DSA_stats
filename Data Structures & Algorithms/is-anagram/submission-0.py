class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts={}
        dictt={}
        for i in range(len(s)):
            if s[i] in dicts:
                dicts[s[i]]=dicts.get(s[i])+1
            else: dicts[s[i]]=int(0)
        for i in range(len(t)):
            if t[i] in dictt:
                dictt[t[i]]=dictt.get(t[i])+1
            else: dictt[t[i]]=int(0)
        return dicts==dictt