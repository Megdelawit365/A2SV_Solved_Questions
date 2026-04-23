class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        curr = 0
        visited = set()

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def inbound(r,c):
            return 0 <= r <= len(grid)-1 and 0 <= c <= len(grid[0])-1

        def dfs(row,col):
            nonlocal curr
            visited.add((row,col))
            curr += 1

            for x,y in directions:
                newr, newc = row + x, col + y
                if not inbound(newr,newc) or grid[newr][newc] == 0:
                    continue
                if (newr,newc) not in visited:
                    dfs(newr,newc)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr = 0
                    dfs(i,j)
                    ans = max(ans,curr)
        
        return ans