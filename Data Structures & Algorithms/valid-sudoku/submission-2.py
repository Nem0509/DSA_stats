class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for r in range(9):
            rchecker=set()
            for c in range(9):
                if board[r][c]!=".":
                    if board[r][c] in rchecker:
                        print(rchecker)
                        return False
                    rchecker.add(board[r][c])
        
        for c in range(9):
            cchecker=set()
            for r in range(9):
                if board[r][c]!=".":
                    if board[r][c] in cchecker:
                        print(cchecker)
                        return False
                    cchecker.add(board[r][c])

        for rc in range(0,len(board),3):
            for cc in range(0,len(board),3):
                cellchecker = set()
                for dr in range(3):          # dr = 0,1,2
                    for dc in range(3):      # dc = 0,1,2
                        val = board[rc+dr][cc+dc]
                        if val!=".":
                            if val in cellchecker:
                                return False
                            cellchecker.add(val)
        return True


