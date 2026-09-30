class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        trapped = 0
        leftMax = height[left]
        righttMax = height[right]
        while left < right:
            if height[left] <= height[right]:
                if leftMax > height[left]:
                    trapped = trapped + (leftMax - height[left])
                left = left + 1
                leftMax = max(leftMax, height[left])
            else: 
                if righttMax > height[right]:
                    trapped = trapped + (righttMax - height[right])
                right = right - 1
                righttMax = max(righttMax, height[right])
        return trapped
                
