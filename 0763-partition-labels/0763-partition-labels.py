class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = defaultdict(int)
        for i,char in enumerate(s):
            lastIdx[char] = i
        left,right = 0,0
        ans = []
        while right < len(s):
            idx = lastIdx[s[left]]
            i = left
            while i < idx + 1:
                if lastIdx[s[i]] > idx:
                    idx = lastIdx[s[i]]
                i += 1
            right = idx + 1
            ans.append(right-left)
            left = right
        return ans

        