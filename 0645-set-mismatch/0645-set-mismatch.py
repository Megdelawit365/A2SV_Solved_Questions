class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = [0,0]
        for n in range(1,len(nums)+1):
            if count[n] == 2:
                ans[0] = n
            if count[n] == 0:
                ans[1] = n
        
        return ans