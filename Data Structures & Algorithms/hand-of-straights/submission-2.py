from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], g: int) -> bool:
        dic=Counter(hand)
        l=min(hand)
        r=max(hand)

        for i in range(l,r+1):
            if dic[i]:
                for j in range(i+1,i+g):
                    if not dic[j]:
                        return False
                    dic[j]-=dic[i]
        
        return True
