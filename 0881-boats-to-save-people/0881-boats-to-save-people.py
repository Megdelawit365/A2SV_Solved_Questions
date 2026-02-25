class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right = 0,len(people)-1
        ans = 0
        while left <= right:
            weight = people[left] + people[right]
            if weight <= limit:
                ans += 1
                left += 1
                right -= 1
            else:
                if people[right] <= limit:
                    ans += 1
                    right -= 1
                elif people[left] <= limit:
                    ans += 1
                    left += 1
        return ans