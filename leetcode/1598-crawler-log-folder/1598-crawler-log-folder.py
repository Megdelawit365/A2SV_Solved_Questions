class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "../" and len(stack) != 0:
                stack.pop(-1)
            elif log == "./" or log == "../" and len(stack) == 0:
                continue
            else:
                stack.append(log)
        return len(stack)
        