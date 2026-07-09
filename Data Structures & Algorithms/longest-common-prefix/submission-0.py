class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=[]
        minlen=200
        for a in strs:
            minlen=min(minlen,len(a))
        for i in range(minlen + 1):
            strs2=[]
            for string in strs:
                if strs2:
                    strs2.append(string[:i])
                    if strs2[-1]!=strs2[-2]:
                        return result[-1] if result else ""
                else:
                    strs2.append(string[:i])

            result.append(strs2[-1]) 
        if result:
            return result[-1]
        else: 
            return ""