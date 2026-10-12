class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        curr_max = 0
        left_idx = 0
        right_idx = len(height) - 1
        while True:
            if curr_max < (right_idx - left_idx)*min(height[left_idx],
                                                     height[right_idx]):
                curr_max = (right_idx - left_idx)*min(height[left_idx],
                                                      height[right_idx])
            if height[left_idx] > height[right_idx]:
                right_idx -= 1
            else:
                left_idx += 1
            if left_idx == right_idx:
                break
        return curr_max
            


if __name__ == '__main__':
    mysol = Solution()
    in_arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(mysol.maxArea(in_arr))
