class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_first_row_zero = False
        is_first_col_zero = False

        for i,n in enumerate(matrix[0]):
            if n == 0:
                is_first_row_zero = True
        for i,n in enumerate(matrix):
            if matrix[i][0] == 0:
                is_first_col_zero = True
        for i in range(1,len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,len(matrix)):
            if matrix[i][0] == 0:
                for j in range(0,len(matrix[i])):
                    matrix[i][j] = 0
        for i in range(1,len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1,len(matrix)):
                    matrix[j][i] = 0
        if is_first_row_zero:
            matrix[0] = [0] * len(matrix[0])
        if is_first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0




