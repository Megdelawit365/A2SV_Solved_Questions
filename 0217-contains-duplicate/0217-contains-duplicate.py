class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = set(nums)
        return len(count) != len(nums)