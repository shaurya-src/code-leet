class Solution:
    def maxArea(self, height: List[int]) -> int:
        # maximize min(x, y) * abs(ix - iy)
        front = 0
        end = len(height) - 1
        max_water = 0
        while front < end:
            h = min(height[front], height[end])
            l = end-front
            curr_water = h*l
            
            max_water = max(curr_water, max_water)
            
            if height[front] > height[end]:
                end -= 1
            else:
                front += 1
        
        return max_water