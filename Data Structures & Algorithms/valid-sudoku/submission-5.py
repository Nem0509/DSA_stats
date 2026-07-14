class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[0]*9
        cols=[0]*9
        square=[0]*9
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c]!=".":
                    i=int(board[r][c])
                    if rows[r] & 1<<(i-1):
                        return False
                    elif cols[c] & 1<<(i-1):
                        return False
                    elif square[3*int(r/3)+int(c/3)] & 1<<(i-1):
                        return False
                    else: 
                        rows[r] |= 1<<(i-1)
                        cols[c] |= 1<<(i-1)
                        square[3*int(r/3)+int(c/3)] |= 1<<(i-1)
        return True
        