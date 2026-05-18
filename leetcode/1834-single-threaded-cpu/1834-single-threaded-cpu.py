class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(en, pr, i) for i, (en, pr) in enumerate(tasks)])
        heap = []
        res = []
        i = 0
        time = 0

        while i < len(tasks) or heap:
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]
            while i < len(tasks) and tasks[i][0] <= time:
                en, pr, idx = tasks[i]
                heapq.heappush(heap, (pr, idx))
                i += 1
            pr, idx = heapq.heappop(heap)
            time += pr
            res.append(idx)
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna