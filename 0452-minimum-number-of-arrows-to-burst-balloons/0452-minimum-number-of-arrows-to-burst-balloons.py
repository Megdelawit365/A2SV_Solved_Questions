class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[1])
        ans = len(points)
        prev = points[0]
        for i in range(1,len(points)):
            if points[i][0] <= prev[1]:
                ans -= 1
            else:
                prev = points[i]
        return ans
        # 1 6
        # 2 8
        # 7 12
        # 10 16

