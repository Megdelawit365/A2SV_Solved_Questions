class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(rooms)):
            for r in rooms[i]:
                graph[i].append(r)
        
        queue = deque()
        queue.append(0)
        open = set()
        open.add(0)

        while queue:
            curr = queue.popleft()
            for i in graph[curr]:
                if i in open:
                    continue
                queue.append(i)
                open.add(i)
        print(open)
        return len(open) == len(rooms)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna