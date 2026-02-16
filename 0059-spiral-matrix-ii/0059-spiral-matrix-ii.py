class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for i in range(n)]
        num = 1
        top,bottom,left,right = 0,n-1,0,n-1
        while num <= n**2:
            for i in range(left,right+1):
                ans[top][i] = num
                num += 1
            
            if n**2 < num:
                break

            for i in range(top+1,bottom+1):
                ans[i][right] = num
                num += 1
            if n**2 < num:
                break
            
            for i in range(right-1,left-1,-1):
                ans[bottom][i] = num
                num += 1
            if n**2 < num:
                break

            for i in range(bottom-1,top,-1):
                ans[i][left] = num
                num += 1
            if n**2 < num:
                break


            top += 1
            bottom -= 1
            left += 1
            right -= 1


        return ans
            
            
        # 1   2    3  4
        # 12  13  14  5
        # 11  16  15  6
        # 10  9    8  7