class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx_nums = []
        for i, num in enumerate(nums):
            idx_nums.append((i, num))
        sorted_nums = sorted(idx_nums, key=lambda x: x[1])
        i = 0
        j = len(sorted_nums) - 1
        while 1:
            if sorted_nums[i][1] + sorted_nums[j][1] == target:
                return [sorted_nums[i][0], sorted_nums[j][0]]
            elif sorted_nums[i][1] + sorted_nums[j][1] > target:
                j -= 1
                continue
            elif sorted_nums[i][1] + sorted_nums[j][1] < target:
                i += 1
                continue


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))
    nums = [3, 2, 4]
    target = 6
    sol = Solution()
    print(sol.twoSum(nums, target))
    nums = [3, 3]
    target = 6
    sol = Solution()
    print(sol.twoSum(nums, target))
