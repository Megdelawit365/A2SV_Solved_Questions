class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        ans = []
        for i in range(row):
            line = []
            for j in range(col):
                sums = 0
                cells = 0
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if i + x in range(0,row) and j + y in range(0,col):
                            sums += img[i+x][j+y]
                            cells += 1
                avg = sums//cells
                line.append(avg)
            ans.append(line)
        return ans
                

                

                
                


