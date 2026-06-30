class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen=set()
            for c in range(9):
                value=board[r][c]
                if value==".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        for c in range(9):
            seen=set()
            for r in range(9):
                value=board[r][c]
                if value==".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen=set()
                for r in range(box_row,box_row+3):
                    for c in range(box_col,box_col+3):
                        value=board[r][c]
                        if value==".":
                            continue
                        if value in seen:
                            return False
                        seen.add(value)
        return True
