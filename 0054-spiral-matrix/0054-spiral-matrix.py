class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # #15
        # matrix[0,0] matrix[0,1] matrix[0,2] matrix[0,3]
        # matrix[3,0] matrix[3,1] matrix[3,2] matrix[3,3]
        # matrix[3,3] matrix[3,2] matrix[3,1] matrix[3,0]
        # matrix[2,0] matrix[2,1]
        ans = []
        top, bottom, left, right = 0,len(matrix),0,len(matrix[0])
        while len(ans) < len(matrix)*len(matrix[0]):
            for i in range(left,right):
                ans.append(matrix[top][i])
            if len(ans) >= len(matrix)*len(matrix[0]):
                break
            for i in range(top+1,bottom):
                ans.append(matrix[i][right-1])
            if len(ans) >= len(matrix)*len(matrix[0]):
                break
            for i in range(right-2,left-1,-1):
                ans.append(matrix[bottom-1][i])
            if len(ans) >= len(matrix)*len(matrix[0]):
                break
            for i in range(left,right-1):
                ans.append(matrix[bottom-2][i])
            if len(ans) >= len(matrix)*len(matrix[0]):
                break
            top += 1
            bottom -= 1
            right -= 1
            left += 1
        return ans



