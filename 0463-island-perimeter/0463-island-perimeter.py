class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def inbound(r,c):
            return 0 <= r <= len(grid)-1 and 0 <= c <= len(grid[0])-1
        visited = set()
        def dfs(row,col):
            nonlocal ans
            visited.add((row,col))
            
            for x,y in directions:
                newr, newc = row + x, col + y
                if not inbound(newr,newc) or grid[newr][newc] == 0:
                    ans += 1
                elif (newr,newc) not in visited:
                    dfs(newr,newc)
        flag = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    flag = True
                    break
            if flag:  break
        
        return ans
