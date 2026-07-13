class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        cnt=[[] for _ in range(len(nums)+1)]
        print(cnt)
        for x,c in dic.items():
            print(x,c)
            cnt[c].append(x)
        print(cnt)
        ans=[]
        for i in range(len(cnt)-1,0,-1):
            if cnt[i]:
                ans+=cnt[i]
                if len(ans)>k:
                    print(ans)
                    break
        while len(ans)>k:
            ans.pop()
        return ans
    


