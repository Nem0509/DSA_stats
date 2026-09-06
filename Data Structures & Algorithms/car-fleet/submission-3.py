class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        nl=[[x,v,(target-x)/v] for x,v in zip(position,speed)]
        sl=sorted(nl,key=lambda x:x[0], reverse=True)

        f=1
        for x in range(1,len(sl)):
            if sl[x][2]<=sl[x-1][2]:
                sl[x][2]=sl[x-1][2]
                continue
            f+=1
        return f


