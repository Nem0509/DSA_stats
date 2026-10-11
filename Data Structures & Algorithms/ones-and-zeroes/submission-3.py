class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count=[]
        for i in range(len(strs)):
            c1=0
            for c in strs[i]:
                if c=='1':
                    c1+=1
            count.append([len(strs[i])-c1,c1])
        print(count)

        dp={}
        def rec(i,c0,c1):
            if i==len(strs):
                return 0
            if (i,c0,c1) in dp:
                return dp[(i,c0,c1)]
            a=count[i][0]
            b=count[i][1]
            if a<=c0 and b<=c1:
                dp[(i,c0,c1)]=max(1+rec(i+1,c0-a,c1-b),rec(i+1,c0,c1))
                return dp[(i,c0,c1)]
            else:
                dp[(i,c0,c1)]=rec(i+1,c0,c1)
                return dp[(i,c0,c1)]

        return rec(0,m,n)
