class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0]*(n+1)
        dp = [0] * (n + 1)


        for x,y in relations:
            graph[x].append(y)
            indegree[y] += 1
        
        queue = deque()
        ans = 0
        for i in range(1,n+1):
            dp[i] = time[i - 1]
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()

            for i in graph[curr]:
                dp[i] = max(dp[i], dp[curr] + time[i - 1])
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        return max(dp)

        