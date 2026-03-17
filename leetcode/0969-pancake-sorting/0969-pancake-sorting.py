class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr),1,-1):
            idx = arr.index(i)
            if idx == i - 1:
                continue
            if idx != 0:
                arr[:idx+1] = reversed(arr[:idx+1])
                ans.append(idx + 1)
            arr[:i] = reversed(arr[:i])
            ans.append(i)
        return ans

