class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        ind = [0]*(numCourses)
        for a,b in prerequisites:
            graph[b].append(a)
            ind[a] += 1
        
        queue = deque()
        for i in range(len(ind)):
            if ind[i] == 0:
                queue.append(i)

        top_order = []
        while queue:
            curr = queue.popleft()
            top_order.append(curr)

            for neigh in graph[curr]:
                ind[neigh] -= 1
                if ind[neigh] == 0:
                    queue.append(neigh)
        
        return top_order if len(top_order) == numCourses else []

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna