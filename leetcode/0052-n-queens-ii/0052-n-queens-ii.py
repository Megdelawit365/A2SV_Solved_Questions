class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["." for _ in range(n)] for _ in range(n)]
        cols = set()
        diag1 = set()
        diag2 = set()
        ans = set()

        def backtrack(r):
            if r == n:
                ans.add(tuple(["".join(row) for row in board]))
                return
            for c in range(n):
                if c in cols or r-c in diag1 or r+c in diag2:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r-c)
                diag2.add(r+c)

                backtrack(r+1)

                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)

        backtrack(0)
        return len(ans)