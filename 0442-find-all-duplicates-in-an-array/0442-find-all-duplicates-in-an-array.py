class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        ans = []
        for key,value in freq.items():
            if value == 2:
                ans.append(key)
        return ans
        
        