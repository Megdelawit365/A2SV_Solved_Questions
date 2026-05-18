class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [n for n in nums]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        return heap[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna