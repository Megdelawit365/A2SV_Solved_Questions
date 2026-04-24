class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def inbound(r,c):
            return 0 <= r <= len(board)-1 and 0 <= c <= len(board[0])-1
        
        visited = set()
        invalid = set()

        def dfs1(row,col):
            invalid.add((row,col))
            
            for x,y in directions:
                newr, newc = row + x, col + y
                if (newr,newc) not in invalid and inbound(newr,newc) and board[newr][newc] == "O":
                    dfs1(newr,newc)
        
        def dfs2(row,col):
            visited.add((row,col))
            board[row][col] = "X"
            for x,y in directions:
                newr, newc = row + x, col + y
                if (newr,newc) not in visited and inbound(newr,newc) and board[newr][newc] == "O":
                    dfs2(newr,newc)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (not inbound(i-1,j-1) or not inbound(i+1,j+1) ):
                    dfs1(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in invalid and inbound(i,j):
                    dfs2(i,j)