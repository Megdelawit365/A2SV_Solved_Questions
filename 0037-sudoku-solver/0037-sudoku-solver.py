class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        def get_box(i, j):
            return (i // 3) * 3 + (j // 3)

        def solve(i,j):
            if i == 9:
                return True
            if j == 8:
                nexti,nextj = i + 1,0
            else:
                nexti,nextj = i, j + 1

            if board[i][j] == ".":
                for ch in "123456789":
                    if ch not in rows[i] and ch not in cols[j] and ch not in boxes[get_box(i,j)]:
                        rows[i].add(ch)
                        cols[j].add(ch)
                        boxes[get_box(i,j)].add(ch)
                        board[i][j] = ch

                        if solve(nexti,nextj):
                            return True

                        board[i][j] = "."
                        rows[i].remove(ch)
                        cols[j].remove(ch)
                        boxes[get_box(i,j)].remove(ch)

            else:
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[get_box(i,j)].add(board[i][j])

                return solve(nexti,nextj)
            
            return False

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    ch = board[i][j]
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[get_box(i, j)].add(ch)
        
        solve(0,0)
        #50