class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        rl = len(matrix) 
        cl = len(matrix[0])
        r = rl*cl - 1

        """


        cv = i % c
        rv = i // r
        r = 3, c =  4
        0 1 2 3       
        4 5 6 7 
        8 9 10 11
        """


        def idx(i):
            return (i // cl,i % cl)



        while l <= r:
            m = (l + r)//2

            row,col = idx(m)
            val = matrix[row][col]

            if  val== target:
                return True
            elif val < target:
                l = m + 1
            else:
                r = m - 1
        return False



        