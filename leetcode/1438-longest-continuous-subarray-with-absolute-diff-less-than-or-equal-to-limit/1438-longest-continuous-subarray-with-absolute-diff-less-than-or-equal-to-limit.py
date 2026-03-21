class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        _min = deque()
        _max = deque()
        l,r = 0, 0
        ans = 0
        

        while r < len(nums):
            while _min and _min[-1] > nums[r]:
                _min.pop()
            _min.append(nums[r])

            while _max and _max[-1] < nums[r]:
                _max.pop()
            _max.append(nums[r])

            while _max[0] - _min[0] > limit:
                if nums[l] == _max[0]:
                    _max.popleft()
                if nums[l] == _min[0]:
                    _min.popleft()
                l += 1
            
            ans = max(ans, r - l + 1)
            r += 1
        return ans
            