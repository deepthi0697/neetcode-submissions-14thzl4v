class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l= 0
        r = len(heights) - 1
       
        while l < r:
            water = min(heights[l],heights[r]) * (abs(l-r))
            max_water = max(max_water,water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water

    # heighti  heightr  water  total
    # 0 - 1        7-6     7    7
    # 0           6 - 3         7