class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        minRemoval = 30
        ans = set()
        def isValid(string):
            stack = []
            for char in string:
                if char == "(": 
                    stack.append("(")
                elif char == ")":
                    if not stack:
                        return False
                    else:
                        stack.pop()
            return len(stack) == 0
        def backtrack(i,path):
            nonlocal minRemoval
            nonlocal ans
            if i == len(s):
                if isValid(path):
                    print(path)
                    diff = len(s) - len(path)
                    if diff < minRemoval:
                        minRemoval = diff
                        ans = {path}
                    elif diff == minRemoval:
                        ans.add(path)
                return
            backtrack(i + 1, path + s[i])

            backtrack(i + 1, path)

        backtrack(0,"")
        if not ans: return [""]
        return list(ans)