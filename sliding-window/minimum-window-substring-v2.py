# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:57:46 2026

@author: patha
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Dictionary to store character frequencies for target string t
        target_counts = Counter(t)
        required_unique = len(target_counts)
        
        # Left and Right pointers for the sliding window
        left, right = 0, 0
        
        # Window character tracker and counter for satisfied unique characters
        window_counts = {}
        satisfied_unique = 0
        
        # Track the minimum window details: (window_length, left_index, right_index)
        ans = (float("inf"), None, None)
        
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If the frequency of the current character matches its target requirement
            if char in target_counts and window_counts[char] == target_counts[char]:
                satisfied_unique += 1
                
            # Contract the window from the left once it satisfies all character criteria
            while left <= right and satisfied_unique == required_unique:
                char_left = s[left]
                
                # Update our minimum window track if this one is smaller
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                    
                # Pop character from left of window
                window_counts[char_left] -= 1
                if char_left in target_counts and window_counts[char_left] < target_counts[char_left]:
                    satisfied_unique -= 1
                    
                left += 1    
            right += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

# Example Execution
if __name__ == "__main__":
    sol = Solution()
    print(f"Minimum Window Substring: {sol.minWindow('ADOBECODEBANC', 'ABC')}") 
    # Output: "BANC"
