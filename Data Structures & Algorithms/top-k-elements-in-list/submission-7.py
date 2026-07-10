class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        lst=[[] for i in range(len(nums)+1)]
        print(dic)
        print(lst)
        for x,f in dic.items():
            lst[f].append(x)
        rst=[]
        print(lst)
        for i in range(len(lst)-1,0,-1):
            for x in lst[i]:
                rst.append(x)
                if len(rst)==k:
                    return rst
