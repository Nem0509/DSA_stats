class MinStack:

    def __init__(self):
        self.arr=[]
        self.minv=float("inf")
        
    def push(self, val: int) -> None:
        if not self.arr:
            self.arr.append(0)
            self.minv=val
        else:
            self.arr.append(val-self.minv)
            if self.arr[-1]<0:
                self.minv=val

    def pop(self) -> None:
        if self.arr[-1]>0:
            self.arr.pop()
        else:
            self.minv-=self.arr.pop()

    def top(self) -> int:
        if self.arr[-1]>0:
            return self.minv+self.arr[-1]
        else:
            return self.minv

    def getMin(self) -> int:
        return self.minv

