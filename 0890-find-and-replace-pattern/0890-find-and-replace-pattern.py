class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # a-a
        # aqq
        # abb
        ans = []
        for word in words:
            map1 = {}
            map2 = {}
            flag = True
            for w,p in zip(word,pattern):
                if w in map1 and map1[w] != p:
                    flag = False
                    break
                elif p in map2 and map2[p] != w:
                    flag = False
                    break
                else:
                    map1[w]  =  p
                    map2[p] = w
            
            if flag:
                ans.append(word)
        return ans     
        