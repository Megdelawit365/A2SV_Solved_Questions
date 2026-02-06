class Solution:
    def intToRoman(self, num: int) -> str:
        string = str(num)
        n = len(string)
        result = ""
        for i,char in enumerate(string):
            if char=='4':
                power = n - i - 1
                remainder = 4 * (10**power)
                if remainder == 400:
                    result += "CD"
                elif remainder == 40:
                    result += "XL"
                elif remainder == 4:
                    result += "IV"
            elif char =='9':
                power = n - i - 1
                remainder = 9 * (10**power)
                if remainder == 900:
                    result += "CM"
                elif remainder == 90:
                    result += "XC"
                elif remainder == 9:
                    result += "IX"
            else:
                power = n - i - 1
                integer = int(char)
                remainder = integer * (10**power)
                while remainder > 0:
                    if remainder >= 1000:
                        remainder -= 1000
                        result += "M"
                    elif remainder >= 500:
                        remainder -= 500
                        result += "D"
                    elif remainder >= 100:
                        remainder -= 100
                        result += "C"
                    elif remainder >= 50:
                        remainder -= 50
                        result += "L"
                    elif remainder >= 10:
                        remainder -= 10
                        result += "X"
                    elif remainder >= 5:
                        remainder -= 5
                        result += "V"
                    elif remainder >= 1:
                        remainder -= 1
                        result += "I"
        return result
            