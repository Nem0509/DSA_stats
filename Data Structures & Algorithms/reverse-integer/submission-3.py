class Solution:
    def reverse(self, x: int) -> int:
        ans,d=0,0
        sign=1
        if x<0:
            sign=-1
            x=x*-1
        
        while x!=0:
            print(ans,x)
            d=x%10
            ans=ans*10+d
            x=x//10
   
        if ans * sign < -2**31 or ans * sign > 2**31 - 1:
            return 0
        else:
            return ans*sign

