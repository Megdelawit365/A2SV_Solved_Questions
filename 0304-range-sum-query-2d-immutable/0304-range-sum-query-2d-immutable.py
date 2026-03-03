class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefSum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            currSum  = []
            for j in range(len(matrix[0])):
                top = self.prefSum[i][j+1]
                left = self.prefSum[i+1][j]
                topLeft = self.prefSum[i][j]
                self.prefSum[i+1][j+1] = matrix[i][j] + top + left - topLeft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,r2,c1,c2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        return self.prefSum[r2][c2] + self.prefSum[r1-1][c1-1] - self.prefSum[r2][c1-1] - self.prefSum[r1-1][c2]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)