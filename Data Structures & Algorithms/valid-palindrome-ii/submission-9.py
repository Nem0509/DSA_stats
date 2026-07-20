class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        cnt=0
        while(i<j):
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower()==s[j].lower():
                    i+=1
                    j-=1
                elif s[i+1].lower()==s[j].lower() and s[i].lower()==s[j-1].lower():
                    return self.validPalindrome1(s) or self.validPalindrome2(s)
                elif s[i+1].lower()==s[j].lower():
                    cnt+=1
                    i+=2
                    j-=1
                    if cnt>1:
                        return False
                elif s[i].lower()==s[j-1].lower():
                    cnt+=1
                    i+=1
                    j-=2
                    if cnt>1:
                        return False
                else:
                    return False
        return True
    
    def validPalindrome1(self, s: str) -> bool:
        i,j=0,len(s)-1
        cnt=0
        while(i<j):
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower()==s[j].lower():
                    i+=1
                    j-=1
                elif s[i+1].lower()==s[j].lower():
                    cnt+=1
                    i+=2
                    j-=1
                    if cnt>1:
                        return False
                elif s[i].lower()==s[j-1].lower():
                    cnt+=1
                    i+=1
                    j-=2
                    if cnt>1:
                        return False
                else:
                    return False
        return True
    
    def validPalindrome2(self, s: str) -> bool:
        i,j=0,len(s)-1
        cnt=0
        while(i<j):
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower()==s[j].lower():
                    i+=1
                    j-=1
                elif s[i].lower()==s[j-1].lower():
                    cnt+=1
                    i+=1
                    j-=2
                    if cnt>1:
                        return False
                elif s[i+1].lower()==s[j].lower():
                    cnt+=1
                    i+=2
                    j-=1
                    if cnt>1:
                        return False

                else:
                    return False
        return True