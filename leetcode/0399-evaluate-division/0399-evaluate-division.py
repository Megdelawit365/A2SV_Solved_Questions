class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        weights = {}
        graph = defaultdict(list)
        ans = []

        for i in range(len(equations)):
            num1, num2 = equations[i][0], equations[i][1]

            graph[num1].append(num2)
            graph[num2].append(num1)

            weights[(num1, num2)] = values[i]
            weights[(num2, num1)] = 1 / values[i]


        # print(graph)
        # print(weights)

        def dfs(src,target,path,visited):
            if src == target:
                return path
            visited.add(src)

            for node in graph[src]:
                if node not in visited:
                    res = dfs(node,target,path*weights[(src, node)],visited)
                    if res != -1:
                        return res

            return -1

        for q in queries:
            if q[0] not in graph or q[1] not in graph:
                ans.append(-1)
                continue
            if  q[0] == q[1]:
                ans.append(1)
            else:
                found = False
                ans.append(dfs(q[0],q[1],1,set()))
        
        return ans
            

        