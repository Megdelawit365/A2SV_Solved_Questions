class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxSize = 0
        maxD = deque()
        minD = deque()

        left = 0
        for right in range(len(nums)):
            while maxD and nums[right] > maxD[-1]:
                maxD.pop()
            maxD.append(nums[right])

            while minD and nums[right] < minD[-1]:
                minD.pop()
            minD.append(nums[right])

            while maxD[0] - minD[0] > limit:
                if nums[left] == maxD[0]:
                    maxD.popleft()
                if nums[left] == minD[0]:
                    minD.popleft()
                left += 1
            maxSize = max(maxSize, right - left + 1)
            
        return maxSize
