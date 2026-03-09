class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        ans =  []
        for char in s:
            if char == "*":
                if len(ans) > 0:
                    ans.pop()
                else:
                    stack.append(char)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    ans.append(char)
        return "".join(ans)