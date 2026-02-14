class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = defaultdict(str)
        map2 = defaultdict(str)
        for i,j in zip(s,t):
            if i in map1 or j in map2:
                if map1[i] != j or map2[j] != i:
                    return False
            else:
                map1[i] = j
                map2[j] = i
        return True