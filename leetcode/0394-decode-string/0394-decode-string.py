class Solution:
    def decodeString(self, s: str) -> str:
        string = ""
        nums = []
        chars = []
        num =  0
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == "[":
                nums.append(num)
                chars.append(string)
                num = 0
                string = ""
            elif char == "]":
                string = chars.pop() + string * nums.pop()
            else:
                string += char
            
        return string