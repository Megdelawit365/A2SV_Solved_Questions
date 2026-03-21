class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                temp = stack.pop()
                ans[temp] = i - temp
            stack.append(i)
        return ans
        # 1 1 0 0 0 0 0 0
        # 2 3 4 