class MyHashMap:

    def __init__(self):
        self.dicc=[]

    def put(self, key: int, value: int) -> None:
        for i in range(0,len(self.dicc)):
            if self.dicc[i][0]==key:
                self.dicc[i][1]=value
                return None
        self.dicc.append([key,value])


    def get(self, key: int) -> int:
        for i in range(0,len(self.dicc)):
            if self.dicc[i][0]==key:
                return self.dicc[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(0,len(self.dicc)):
            if self.dicc[i][0]==key:
                del self.dicc[i]
                break
                  


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)