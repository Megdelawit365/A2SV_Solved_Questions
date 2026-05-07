class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        colors = [0]*len(graph)
        visited = set()

        def dfs(node, color):
            visited.add(node)
            colors[node] = color
            
            for n in graph[node]:
                if n in visited and colors[n] == colors[node]:
                    return False
                if n not in visited:
                    if not dfs(n, not color):
                        return False
            
            return True

        
        for i in range(len(graph)):
            if i not in visited:
                if not dfs(i,0):
                    return False
    
        return True
        

        
            

