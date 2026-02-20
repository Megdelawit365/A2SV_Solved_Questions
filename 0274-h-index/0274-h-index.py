class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 0 1 2 3 4 5
        # 0 4 3 3 2 2 
        # 3 2 2 1 1
        # 1 2 3
        # 2 1 1
        count = [0]*(len(citations)+1)
        for c in citations:
            for i in range(1,c+1):
                count[i]+=1
                if i == len(count)-1:
                    break
        maxValue = 0
        # return count
        for i in range(1,len(count)):
            if count[i] >= i and i != 0:
                maxValue = max(maxValue,i)
            
        return maxValue