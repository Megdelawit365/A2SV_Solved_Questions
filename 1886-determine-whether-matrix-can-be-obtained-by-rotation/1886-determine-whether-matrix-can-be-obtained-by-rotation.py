class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        equalCells = []

        flag = False
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    flag = True
                    break
            if flag:
                break
        if not flag:
            return True

        flag = False
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[j][n-1-i]:
                    flag = True
                    break
            if flag:
                break
        if not flag:
            return True

        flag = False
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n-1-i][n-1-j]:
                    flag = True
                    break
            if flag:
                break
        if not flag:
            return True

        flag = False
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n-1-j][i]:
                    flag = True
                    break
            if flag:
                break
        if not flag:
            return True
        else:
            return False

        