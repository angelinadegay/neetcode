class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        rightMax = height[len(height) - 1]

        total_water = 0


        left = 1
        right = len(height) - 2

        while left <= right:
            if leftMax < rightMax:
                leftMax = max(height[left], leftMax)
                current = leftMax - height[left]
                left += 1
                
            else:
                rightMax = max(height[right], rightMax)
                current = rightMax - height[right]
                right -= 1


            total_water = total_water + current


        return total_water
            
                    