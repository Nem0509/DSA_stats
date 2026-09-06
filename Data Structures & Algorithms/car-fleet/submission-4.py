class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        nl=[[x,v] for x,v in zip(position,speed)]
        nl.sort(key=lambda x: x[0], reverse=True)
        ans=[]
        ans.append((target-nl[0][0])/nl[0][1])
        for x in range(1,len(nl)):
            if (target-nl[x][0])/nl[x][1]<=ans[-1]:
                continue
            ans.append((target-nl[x][0])/nl[x][1])
            
        return len(ans)


