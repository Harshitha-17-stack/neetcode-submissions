class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        t,b = 0, ROWS-1

        while t <= b:
            m = t + (b-t) // 2

            if target < matrix[m][0]:
                b = m-1
            elif target > matrix[m][-1]:
                t = m+1
            else:
                break
        
        row = m

        l,r = 0, COLS-1
        while l <= r:
            m = l + (r-l) // 2

            if target < matrix[row][m]:
                r = m-1
            elif target > matrix[row][m]:
                l = m+1
            elif target == matrix[row][m]:
                return True
        return False