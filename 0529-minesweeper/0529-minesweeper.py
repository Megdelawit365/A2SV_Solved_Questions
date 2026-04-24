class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        def inbound(r,c):
            return 0 <= r <= len(board)-1 and 0 <= c <= len(board[0])-1


        def play(row,col):
            print(row,col)
            if board[row][col] == "M":
                board[row][col] = "X"
                return
            elif board[row][col] == "E":
                count = 0
                for x,y in directions:
                    newr, newc = row + x, col + y
                    if inbound(newr,newc) and board[newr][newc] == "M":
                        count += 1

                if count == 0:
                    board[row][col] = "B"
                    for x,y in directions:
                        newr, newc = row + x, col + y
                        if inbound(newr,newc) and board[newr][newc] == "E":
                            play(newr,newc)
                else: 
                    board[row][col] = str(count)
                    return

        play(click[0],click[1])
        return board