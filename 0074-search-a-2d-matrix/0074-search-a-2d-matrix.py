class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1
        while l <= r:
            mid = l + (r-l)//2
            if (target >= matrix[mid][0] and target <= matrix[mid][-1]) or l == r:
                left,right = 0,len(matrix[mid])-1
                while left <= right:
                    m = left + (right-left)//2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] > target:
                        right = m - 1
                    else:
                        left = m + 1
                return False
            
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
            
        return False