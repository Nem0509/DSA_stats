class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans=[0]*len(temp)
        for i in range(len(temp)-2,-1,-1):
            j=i+1
            while temp[j]<=temp[i]:
                if ans[j]==0:
                    break
                j+=ans[j]
            if temp[j]>temp[i]:
                ans[i]=j-i

        return ans