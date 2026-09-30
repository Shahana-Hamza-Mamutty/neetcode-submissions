class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        start = 0
        end =  len(heights) - 1

        while start < end:
            h1, h2 = heights[start], heights[end]
            area =  (end - start) * min(h1, h2)
            if area > max_area:
                max_area = area
            
            if h1 <= h2:
                start = start + 1
            elif h2 < h1:
                end = end - 1
        
        return max_area