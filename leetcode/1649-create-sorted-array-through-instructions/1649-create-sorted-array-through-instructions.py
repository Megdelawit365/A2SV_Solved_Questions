class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        ans = 0
        nums = []
        for i in instructions:
            less = bisect_left(nums, i)
            greater = len(nums) - bisect_right(nums, i)

            ans += min(less, greater)
            nums.insert(less, i)

        return ans % (10**9 + 7)