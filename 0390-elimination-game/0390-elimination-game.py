class Solution:
    def lastRemaining(self, n: int) -> int:
        nums = set(list(range(1,n+1)))
        print(nums)
        def helper(direction, low, high, step):
            if len(nums) == 1:
                return nums.pop()
            ans = 0
            if direction == "left":
                for i in range(low,high+1,step):
                    nums.remove(i)
                if high % 2 != 0:
                    high -= 1
                ans = helper("right",low+1,high,step+2)
            else:
                for i in range(high,low-1,-step):
                    nums.remove(i)
                if low % 2 != 0:
                    low += 1
                ans = helper("left",low,high-1,step+2)
            
            return ans
        
        return helper("left",1,n,2)
        


                    
