class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        ans = 0

        for i in range(len(isConnected)):
            if sum(isConnected[i]) == 1:
                graph[i+1] = []
                continue
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    graph[i+1].append(j+1)
                    graph[j+1].append(i+1)

        # print(graph)
        
        def dfs(node):
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)
            return

        for i,j in graph.items():
            if i not in visited:
                dfs(i)
                ans += 1

        return ans
        # 1 1 0
        # 1 1 0
        # 0 0 1

        # 1 -> 2
        # 2 -> 1