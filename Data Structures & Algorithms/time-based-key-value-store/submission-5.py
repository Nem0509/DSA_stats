class TimeMap:

    def __init__(self):
        self.timemap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key]=[]
        self.timemap[key].append([timestamp,value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        r=len(self.timemap[key])-1
        l=0
        if timestamp>=self.timemap[key][r][0]:
            return self.timemap[key][r][1]
        if timestamp<self.timemap[key][l][0]:
            return ""
        while l<=r:
            m=l+(r-l)//2

            if self.timemap[key][m][0]==timestamp:
                return self.timemap[key][m][1]
            elif self.timemap[key][m][0]<timestamp:
                l=m+1
            else:
                r=m-1
        return self.timemap[key][r][1]

