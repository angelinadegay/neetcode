class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            width = right - left
            new_area = min(heights[left], heights[right]) * width
            max_area = max(new_area, max_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area

       