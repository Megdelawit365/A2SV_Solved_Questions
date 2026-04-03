class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 0 1 2 3 4 5 6 7 8 9
        ans = []
        n = len(s)
        def backtrack(idx, path):
            if idx == n:
                print(idx)
                ans.append(" ".join(path))
                return
            for i in range(idx,n):
                if s[idx:i+1] not in wordDict:
                    continue
                path.append(s[idx:i+1])
                backtrack(i+1,path)
                path.pop()
        
        backtrack(0,[])
        return ans
                
