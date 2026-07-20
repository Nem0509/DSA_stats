class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        l=min(len(word1),len(word2))
        for i in range(2*l):
            if i%2==0:
                ans.append(word1[int(i//2)])
            else:
                ans.append(word2[int(i//2)])
        if len(word1)<len(word2):
            for i in range(l,len(word2)):
                ans.append(word2[i])
        else:
            for i in range(l,len(word1)):
                ans.append(word1[i])

        return "".join(ans)
