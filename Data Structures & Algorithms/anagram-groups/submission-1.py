class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for s in strs:
            t=[0]*26    
            for l in s:
                t[ord(l)-ord("a")]+=1    
            dic[tuple(t)].append(s)
        return list(dic.values())