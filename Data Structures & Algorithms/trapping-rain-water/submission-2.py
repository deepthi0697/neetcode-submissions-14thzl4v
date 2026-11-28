class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0       
        maxRight = 0
        l = 0
        r = len(height) - 1

        totalWaterTrap = 0

        while l <= r:
            
            maxLeft = max(height[l], maxLeft)
            maxRight = max(height[r], maxRight)
            if maxLeft <= maxRight:
                totalWaterTrap += min(maxLeft, maxRight) - height[l]
                l+=1
            else:
                totalWaterTrap += min(maxLeft, maxRight) - height[r]
                r-=1


        return totalWaterTrap
            
            
