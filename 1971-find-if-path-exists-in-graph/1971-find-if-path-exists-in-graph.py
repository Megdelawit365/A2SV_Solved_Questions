class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node, visited):
            if node == destination:
                return True
            
            for n in graph[node]:
                if n in visited:
                    continue
                visited.add(n)
                if dfs(n, visited):
                    return True
                 
            return False
        
        if dfs(source, set()):
            return True
        
        return False