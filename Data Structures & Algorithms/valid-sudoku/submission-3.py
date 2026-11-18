class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ln = len(board[0])
        row = [set() for _ in range(ln)]
        col = [set() for _ in range(ln)]
        box = [set() for _ in range(ln)]

        def boxIdx(r,c):
            boxr = math.floor((r )/3)
            boxc = math.floor((c)/3)
            """
            0  1 => 0 + 3* 1 = 3
            """
            boxNo = boxr + 3 * boxc
            return boxNo
        
        for r in range(ln):
            for c in range(ln):
                val = board[r][c]
                if val == ".":
                    continue
                boxIndex = boxIdx(r,c)
                if val in row[r] or val in col[c] or val in box[boxIndex]:
                    return False
                row[r].add(val)
                col[c].add(val)
                box[boxIdx(r,c)].add(val)
        return True



        