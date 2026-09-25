class Solution:
    def mergeTriplets(self, tr: List[List[int]], ta: List[int]) -> bool:
        i1=None
        i2=None
        i3=None
        for i in range(len(tr)):
            if tr[i][0]==ta[0] and tr[i][1]<=ta[1] and tr[i][2]<=ta[2]:
                i1=i
            if tr[i][1]==ta[1] and tr[i][0]<=ta[0] and tr[i][2]<=ta[2]:
                i2=i
            if tr[i][2]==ta[2] and tr[i][1]<=ta[1] and tr[i][0]<=ta[0]:
                i3=i
        print(i1,i2,i3)
        if i1 is not None and i2 is not None and i3 is not None:
            return True
        return False

            