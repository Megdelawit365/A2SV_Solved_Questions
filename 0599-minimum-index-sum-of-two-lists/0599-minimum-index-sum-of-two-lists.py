class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        freq1 = {}
        freq2 = {}
        minSum = 1001
        common = []
        for i,s in enumerate(list1):
            if s in freq1:
                continue
            else:
                freq1[s] = i
        for i,s in enumerate(list2):
            if s in freq2:
                continue
            else:
                freq2[s] = i
        for s in list1:
            if s in freq1 and s in freq2:
                indexSum = freq1[s] + freq2[s]
                minSum = min(minSum, indexSum)
                common.append([freq1[s], freq2[s]])
        ans = []
        for c in common:
            if c[0] + c[1] == minSum:
                ans.append(list1[c[0]])
        return ans

        