class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        for char in s:
            if char in match.keys():
                stack.append(char)
            elif len(stack) > 0 and match[stack[-1]] == char:
                stack.pop()
            else:
                return False
        if len(stack) > 0 :
            return False
        return True