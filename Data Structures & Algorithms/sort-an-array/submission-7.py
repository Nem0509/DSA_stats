class Solution:
    def sortArray(self,arr):
        self.heapsort(arr)
        return arr
    
    def heapsort(self,arr):
        for i in range(len(arr)//2,0,-1):
            self.heapify(arr,i,len(arr))
        for i in range(len(arr),1,-1):
            arr[0],arr[i-1]=arr[i-1],arr[0]
            self.heapify(arr,1,i-1)
            
    def heapify(self,arr,i,n):
        largest=i
        left=2*i
        right=2*i+1
        if left<=n and arr[left-1]>arr[largest-1]:
            largest=left
        if right<=n and arr[right-1]>arr[largest-1]:
            largest=right
        if largest!=i:
            arr[i-1],arr[largest-1]=arr[largest-1],arr[i-1]
            self.heapify(arr,largest,n)