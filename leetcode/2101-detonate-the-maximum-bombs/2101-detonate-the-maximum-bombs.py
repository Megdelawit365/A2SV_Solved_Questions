class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                bomb1 = bombs[i]
                bomb2 = bombs[j]

                if math.dist([bomb1[0],bomb1[1]],[bomb2[0],bomb2[1]]) <= bomb1[2]:
                    graph[i].append(j)
                if math.dist([bomb1[0],bomb1[1]],[bomb2[0],bomb2[1]]) <= bomb2[2]:
                    graph[j].append(i)
     
        print(graph)

        def dfs(node,visited,path):
            visited.add(node)
            path.add(node)
            for n in graph[node]:
                path.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n,visited,path)
            return len(visited)
        
        ans = 0
        for i in range(len(bombs)):
            ans = max(dfs(i,set(),set()),ans)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna