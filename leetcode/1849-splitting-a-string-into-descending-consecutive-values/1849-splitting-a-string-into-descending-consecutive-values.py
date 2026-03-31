class Solution:
    def splitString(self, s: str) -> bool:
        
        def split(i,path):
            if i == len(s):
                for j in range(1,len(path)):
                    if path[j] != path[j-1] - 1:
                        return False
                return len(path) >= 2

            for j in range(i,len(s)):
                val = int(s[i:j+1])
                path.append(val)
                if split(j+1,path):
                    return True
                path.pop()
            return False
        return split(0,[])