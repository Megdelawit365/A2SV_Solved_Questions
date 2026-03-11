class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []

        for i in range(k):
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
        ans.append(q[0])

        left = 0

        for right in range(k,len(nums)):
            while q and nums[right] > q[-1]:
                q.pop()
            q.append(nums[right])
            while right - left + 1 > k:
                if nums[left] == q[0]:
                    q.popleft()
                left += 1
            ans.append(q[0])
        return ans