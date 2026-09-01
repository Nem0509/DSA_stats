class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        
        mapp={"(":")","[":"]","{":"}"}
        stack=[]

        for x in range(len(s)):
            print(stack)
            if len(stack)>0 and s[x]==mapp.get(stack[-1]):
                stack.pop()
            else:
                stack.append(s[x])

        if stack==[]:
            return True
        else:
            return False