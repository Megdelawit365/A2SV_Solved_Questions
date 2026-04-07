class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1],[1,1]]
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 0:
            return [1]
        for i in range(2,rowIndex+1):
            curr = []
            for j in range(len(ans[-1])):
                if j == 0: 
                    curr.append(ans[-1][j])
                    continue
                curr.append(ans[-1][j-1] + ans[-1][j])
                if j == len(ans[-1])-1:
                    curr.append(ans[-1][j])
            ans.append(curr)
        return ans[-1]