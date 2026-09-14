class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        check=0
        for a in allowed:
            check|=(1<<(ord(a)-ord('a')))

        ans=len(words)
        for w in words:
            for c in w:
                if not (1<<(ord(c)-ord('a')))&check:
                    ans-=1
                    break
        return ans
                
