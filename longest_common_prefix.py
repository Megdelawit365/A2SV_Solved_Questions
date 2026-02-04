class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i,char in enumerate(strs[0]):
            for j in range(1,len(strs)):
                if i>len(strs[j]) or strs[j][0:i+1] != strs[0][0:i+1]:
                    return ans
            ans += char
        return ans

#6.20