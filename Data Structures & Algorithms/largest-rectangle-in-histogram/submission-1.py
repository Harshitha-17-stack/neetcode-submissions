# heights = [7,1,7,2,2,4]
# output: 8

# stack = []
# i = 6
# height = 1, width = 1
# maxArea = 8

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int: # [7,1,7,2,2,4]
        n = len(heights)
        stack = [] # stack = []
        maxArea = 0

        for i in range(len(heights)+1): # i = 6
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()] # height = 1
                # (i-1) - (stack[-1]+1) + 1 
                width = i if not stack else i - stack[-1] -1  # width = 1
                maxArea = max(maxArea, height * width) # maxArea = 8
            
            stack.append(i)
        
        return maxArea # 8
        