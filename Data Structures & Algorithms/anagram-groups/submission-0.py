class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for s in strs:
            t=[0]*26    
            for l in s:
                t[ord(l)-ord("a")]+=1
            if tuple(t) in dic:
                dic[tuple(t)].append(s)
            else:
                dic[tuple(t)]=[s]
        return list(dic.values())