class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])

        visited = set()
        
        def bfs(node,ansc):
            visited.add(node)
            for j in graph[node]:
                ans[j].add(ansc)
                if j not in visited:
                    bfs(j,ansc)


        for i in range(n):
            visited = set()
            bfs(i,i)

        for i in range(len(ans)):
            ans[i] =  sorted(list(ans[i]))
        
        return ans

