class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        row_len = len(matrix)
        col_len = len(matrix[0])

        right = (row_len * col_len) - 1
        
        def idx(i):
            r = i // col_len
            c = i % col_len
            return (r,c)
        while left <= right:
            mid = (left+right) // 2

            r,c = idx(mid)
            val =  matrix[r][c]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        