class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=0
        c1=0
        b=0
        c2=0
        for i in nums:
            if i==a:
                c1+=1
            elif i==b:
                c2+=1
            elif c1==0:
                a=i
                c1+=1
            elif c2==0:
                b=i
                c2+=1
            else:
                c1-=1
                c2-=1
        ans=[]
        if nums.count(a)>int(len(nums)/3):
            ans.append(a)
        if nums.count(b)>int(len(nums)/3):
            ans.append(b)
        return ans
            