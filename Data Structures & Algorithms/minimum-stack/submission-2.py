class MinStack:

    def __init__(self):
        self.arr=[]
        self.minv=float("inf")

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.minv=min(self.minv,val)

    def pop(self) -> None:
        if self.arr[-1]==self.minv:
            self.arr.pop()
            temp=[]
            self.minv=float("inf")
            while len(self.arr):
                self.minv=min(self.minv,self.arr[-1])
                temp.append(self.arr.pop())
            while len(temp):
                self.arr.append(temp.pop())
        else:
            self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minv
