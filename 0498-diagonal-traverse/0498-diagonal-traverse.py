class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        diagonals = row + col - 1
        up = True
        ans = []
        for i in range(diagonals):
            nums = []
            for j in range(len(mat)):
                c = i - j
                if c >= 0 and c < len(mat[0]):
                    nums.append(mat[j][c])
            if not up:
                ans += nums
            else:
                ans += reversed(nums)
            up = not up
        return ans
                    





        # # 1  2  3  4
        # # 5  6  7  8
        # # 9  10 11 12
        # # 13 14 15 16
        # # mat[0][0] 
        # # mat[0][1] mat[1][0]
        # # mat[2][0] mat[1][1] mat[0][2]
        # # mat[1][2] mat[2][1]
        # # mat[2,2]

        # # mat[0][0] 
        # # mat[0][1] mat[1][0]
        # # mat[2][0] mat[1][1] mat[0][2]
        # # mat[0][3] mat[1][2] mat[2][1] mat[3][0]
        # # mat[1][2] mat[2][1]
        # # mat[2,2]
        
        # # i   up      j
        # # 0   true    [0,i+1]
        # # 1   false   [0,i][i,0]
        # # 2   true    [i,0][0,i]

        # # mat[0][0] 
        # # mat[0][1] mat[1][0]
        # # mat[2][0] mat[1][1] mat[0][2]
        # # mat[1][2] mat[2][1]
        # # mat[2,2]

        # # 1 2  3  4 
        # # 5 6  7  8
        # # 9 10 11 12

        # # mat[0][0] 
        # # mat[0][1] mat[1][0]
        # # mat[2][0] mat[1][1] mat[0][2]
        # # mat[0][3] mat[1][2] mat[2][1]
        # # mat[2][2] mat[1][2]
        # # mat[2,3]

        # up = True
        # ans = []
        # for i in range(len(mat[0])):
        #     j = i
        #     for k in range(0,i+1):
        #         if up:
        #             if j >= len(mat):
        #                 break
        #             ans.append(mat[j][k])
        #         else:
        #             if k >= len(mat):
        #                 break
        #             ans.append(mat[k][j])
        #         j -= 1
        #     up = not up
        # up = False
        
        # for i in range(1,len(mat[0])):
        #     j = len(mat[0]) - 1
        #     for k in range(i,len(mat[0])):
        #         if up:
        #             if j >= len(mat):
        #                 break
        #             ans.append(mat[j][k])
        #         else:
        #             if k >= len(mat):
        #                 break
        #             ans.append(mat[k][j])
        #         j -= 1
        #     up = not up
        
        # return ans
