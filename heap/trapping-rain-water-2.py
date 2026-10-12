# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:51:12 2026

@author: patha
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            # The water level is limited by the smaller boundary wall
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
                
        return water_trapped

# Example verification to log into your daily TIL repo tracker
if __name__ == "__main__":
    sol = Solution()
    elevation_map = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"Total Trapped Rainwater: {sol.trap(elevation_map)}") # Output: 6
