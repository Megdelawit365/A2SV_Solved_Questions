class Solution:
    def lastRemaining(self, n: int) -> int:
        def helper(dir, num):
            if num == 1:
                return 1
            if dir == "left":
                return 2 * helper("right", num//2)
            else:
                if num % 2 == 0:
                    return 2 * helper("left", num//2) - 1
                return 2 * helper("left", num//2)
        
        return helper("left", n)
       
         
