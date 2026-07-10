class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.cummatrix = [[0]*(self.cols+1) for _ in range(self.rows+1)]
        
        for r in range(1, self.rows+1):
            for c in range(1, self.cols+1):
                self.cummatrix[r][c] = (
                    matrix[r-1][c-1]
                    + self.cummatrix[r-1][c]
                    + self.cummatrix[r][c-1]
                    - self.cummatrix[r-1][c-1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.cummatrix[row2+1][col2+1]
            - self.cummatrix[row1][col2+1]
            - self.cummatrix[row2+1][col1]
            + self.cummatrix[row1][col1]
        )
