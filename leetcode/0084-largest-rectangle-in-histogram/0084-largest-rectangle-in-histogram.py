class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        maxSize = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                h = heights[idx]
                width = 0
                if len(stack) == 0:
                    # means the height we popped is smaller than all the heights before it
                    width = i
                else:
                    # this is for a stack consisting of non consecutive indices. like when there are 2 equal heights and there's a bigger height in the middle
                    width = i - stack[-1] - 1
                area = h * width
                maxSize = max(maxSize, area)
            stack.append(i)            
        return maxSize

        
