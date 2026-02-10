class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans = []
        # 1 2 3 4 6 8
        i = 0
        while i < len(changed):
            n = changed[i]
            if i == 1:
                return n
            if n*2 in changed[i+1:]:
                ans.append(n)
                changed.remove(n)
                changed.remove(n*2)
            else:
                return []
        return ans
        #16

                    