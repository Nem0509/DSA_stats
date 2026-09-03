
class MinStack:

    def __init__(self):
        self.stack=[]
        self.pre=[]

    def push(self, val: int) -> None:
        if len(self.pre) and self.pre[-1]>=val:
            self.pre.append(val)
        elif len(self.pre)==0:
            self.pre.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1]==self.pre[-1]:
            self.pre.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pre[-1]
