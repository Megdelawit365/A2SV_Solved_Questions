class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {}
        for i in range(len(names)):
            hashmap[heights[i]] = names[i]
        for i in range(len(names)):
            for j in range(i,len(names)):
                if heights[i] < heights[j]:
                    heights[i], heights[j] = heights[j], heights[i]
        ans = []
        for h in heights:
            ans.append(hashmap[h])
        return ans
        