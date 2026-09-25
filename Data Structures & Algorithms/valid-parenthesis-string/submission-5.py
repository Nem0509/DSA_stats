class Solution:
    def checkValidString(self, s: str) -> bool:
        ls=[]
        ss=[]
        for i,c in enumerate(s):
            if c=='(':
                ls.append([i,c])
            elif c=='*':
                ss.append([i,c])
            else:
                if ls:
                    ls.pop()
                elif ss:
                    ss.pop()
                else:
                    return False
        if ls:
            while ls and ss and ls[-1][0]<ss[-1][0]:
                ls.pop()
                ss.pop()
        if not ls:
            return True
        return False