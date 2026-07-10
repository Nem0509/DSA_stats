class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            elif i in dic:
                dic[i]+=1
        lst=[]
        for x,f in dic.items():
            lst.append([f,x])
        lst.sort()
        result=[]
        for k in range(1,k+1):
            result.append(lst[-k][-1])
        return result
