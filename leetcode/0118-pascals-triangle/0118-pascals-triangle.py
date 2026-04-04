class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        if numRows == 2:
            return [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        for i in range(3,numRows+1):
            curr = []
            for j in range(len(ans[-1])):
                if j == 0: 
                    curr.append(ans[-1][j])
                    continue
                curr.append(ans[-1][j-1] + ans[-1][j])
                if j == len(ans[-1])-1:
                    curr.append(ans[-1][j])
            ans.append(curr)
        return ans                

