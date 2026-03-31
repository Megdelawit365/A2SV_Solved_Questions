class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def split(i,path):
            if i == len(num):
                return len(path) >= 3

            for j in range(i,len(num)):
                if num[i] == '0' and j > i:
                    break
                val = int(num[i:j+1])
                path.append(val)
                if len(path) >= 3:
                    if path[-1] != path[-2] + path[-3]:
                        path.pop()
                        continue
                if split(j+1,path):
                    return True
                path.pop()
            return False
        return split(0,[])