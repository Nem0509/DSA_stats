class MinStack:

    def __init__(self):
        self.arr=[]
        self.minv=float("inf")

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.minv=min(self.minv,val)

    def pop(self) -> None:
        if self.arr[-1]==self.minv:
            self.minv=float("inf")
            for x in range(0,len(self.arr)-1):
                self.minv=min(self.minv,self.arr[x])
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minv
