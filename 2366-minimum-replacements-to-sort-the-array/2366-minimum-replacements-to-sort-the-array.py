class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev = nums[-1]
        ans = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                k = nums[i] // prev
                if nums[i] % prev != 0:
                    k += 1
                ans += k - 1
                prev = nums[i] // k
        return ans