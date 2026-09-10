class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l=0
        col=len(matrix[0])
        row=len(matrix)
        r=row*col-1
        while l<=r:
            m= l + (r-l)//2
            if matrix[m//col][m%col]==target:
                return True
            elif matrix[m//col][m%col]>target:
                r=m-1
            elif matrix[m//col][m%col]<target:
                l=m+1
        return False





