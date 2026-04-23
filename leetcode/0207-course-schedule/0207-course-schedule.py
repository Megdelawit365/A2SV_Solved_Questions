class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i,j in prerequisites:
            graph[i].append(j)
        white, grey, black = 0,1,2
        colors = [white]*numCourses
        cycle = False
        def dfs(node):
            nonlocal cycle
            if cycle:
                return
            colors[node] = grey
            if node in graph:
                for nei in graph[node]:
                    if colors[nei] == white:
                        dfs(nei)
                    elif colors[nei] == grey:
                        cycle = True
            
            colors[node] = black

        
        for i in range(numCourses):
            if colors[i] == white:
                dfs(i)
        return not cycle

