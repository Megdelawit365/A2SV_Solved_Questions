class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0],nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow)

        slow = nums[0];
        while slow != fast: 
            slow = nums[slow]
            fast = nums[fast]
        return slow

    
        # 1 -> 3 -> 2 -> 4 -> 2
        # 1 1
        # 3 2
        # 2 2
        # 4
        
