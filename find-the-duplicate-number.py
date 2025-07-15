from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
        There is only one repeated number in nums, return this repeated number.
        You must solve the problem without modifying the array nums and using only constant extra space.
        """
        # Phase 1: Find the intersection point of the two runners (Floyd's Tortoise and Hare).
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
                
        # Phase 2: Find the entrance to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            
        return hare
