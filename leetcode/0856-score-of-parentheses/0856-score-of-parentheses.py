class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for ch in s:
            if ch == '(':
                stack.append(score)
                score = 0
            else:
                score += stack[-1] + max(1,score)
                stack.pop()
        return score

       