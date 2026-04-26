class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = set()

        def dfs(node,path):
            if node in path:
                return False
            if not graph[node] or node in safe:
                return True
            
            path.add(node)

            for n in graph[node]:
                if not dfs(n,path):
                    return False
            path.remove(node)
            
            safe.add(node)
            return True


        for i in range(len(graph)):
            if dfs(i,set()):
                safe.add(i)
        return sorted(list(safe))