class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        top, bottom, left, right = rStart, rStart + 1, cStart, cStart + 1
        ans = []
        while len(ans) < rows*cols:
            for i in range(left,right+1):
                if i not in range(0,cols) or top not in range(0,rows):
                    continue
                ans.append([top,i])
            for i in range(top+1,bottom+1):
                if right not in range(0,cols) or i not in range(0,rows):
                    continue
                ans.append([i,right])
            for i in range(right-1,left-2,-1):
                if i not in range(0,cols) or bottom not in range(0,rows):
                    continue
                ans.append([bottom,i])
            top -= 1
            left -= 1
            for i in range(bottom - 1, top, -1):
                if i not in range(0,rows) or left not in range(0,cols):
                    continue
                ans.append([i,left])
            right += 1
            bottom += 1
        return ans