class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        divisions = defaultdict(int)

        def dfs(node,color):
            visited.add(node)
            divisions[node] = color

            for nei in graph[node]:
                if nei in visited and divisions[nei] == color:
                    return False
                if nei not in visited:
                    if not dfs(nei,not color):
                        return False
            
            return True

        for i in range(len(graph)):
            if i not in visited and not dfs(i,0):
                return False

        return True
