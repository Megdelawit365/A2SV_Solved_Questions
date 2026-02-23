class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        i,j = 0,1
        if len(arr) < 2:
            return True
        while j < len(arr):
            if arr[j] < arr[i]:
                return False
            i += 1
            j += 1
        return True