class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
            
        # Calculate suffix products and combine
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
            
        return answer

if __name__ == '__main__':
    sol = Solution()
    
    nums1 = [1, 2, 3, 4]
    print("Test 1 - Expected: [24, 12, 8, 6], Got:", sol.productExceptSelf(nums1))
    
    nums2 = [-1, 1, 0, -3, 3]
    print("Test 2 - Expected: [0, 0, 9, 0, 0], Got:", sol.productExceptSelf(nums2))
