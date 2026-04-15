class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i1,j1 = len(matrix)-1,0

        while i1 >= 0 and j1 <= len(matrix[0])-1:
            if target == matrix[i1][j1]:
                return True
            
            if target > matrix[i1][j1]:
                j1 += 1 
            else:
                i1 -= 1

        return False