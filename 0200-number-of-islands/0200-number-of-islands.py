class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()

        def dfs(row,col):

            visited.add((row,col))

            for x,y in directions:
                newr, newc = row + x, col + y
                if inbound(newr,newc) and (newr,newc) not in visited and grid[newr][newc] == "1":
                    dfs(newr,newc)
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i,j)
                    ans += 1

        return ans