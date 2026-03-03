class Solution:
    def atMostKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        count = defaultdict(int)
        for right in range(len(nums)):
            count[nums[right]] += 1
            while len(count) > k :
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]] 
                left += 1
            ans += right - left + 1
        return ans

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostKDistinct(nums,k) - self.atMostKDistinct(nums,k-1)