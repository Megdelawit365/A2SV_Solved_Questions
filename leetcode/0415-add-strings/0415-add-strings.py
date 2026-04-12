class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1,num2 = num2,num1

        num1 = "".join(list(reversed(num1)))
        num2 = "".join(list(reversed(num2)))

        carry = 0
        ans  = ""

        for i in range(len(num1)):
            if i >= len(num2):
                curr = int(num1[i]) + carry
            else:
                curr = int(num1[i]) + int(num2[i]) + carry
            ans += str(curr % 10)
            carry = curr // 10

        if carry:
            ans += str(carry)
        return "".join(list(reversed(ans)))