class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        l,r = 1, (max(position) - min(position))
        position.sort()

        while l <= r:
            mid = l + (r-l)//2
            left,right = 1,len(position)
            prev = position[0]
            count = 1
            while left < right:
                if position[left] - prev >= mid:
                    prev = position[left]
                    count += 1
                left += 1
            if count < m:
                r = mid - 1
            else:
                l = mid + 1

        return r


            
