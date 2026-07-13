class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.presum=self.summat(matrix)
    
    def summat(self, matrix):
        presum=[[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        for i in range(1,len(presum)):
            for j in range(1,len(presum[0])):
                presum[i][j]=matrix[i-1][j-1]+presum[i-1][j]+presum[i][j-1]-presum[i-1][j-1]
        return presum
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=self.presum[row2+1][col2+1]-self.presum[row2+1][col1]-self.presum[row1][col2+1]+self.presum[row1][col1]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)