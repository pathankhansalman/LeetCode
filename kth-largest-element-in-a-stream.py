class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = list(reversed(sorted(nums)))[:k]
        self.k = k
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.nums = list(reversed(sorted(self.nums)))
        elif val > self.nums[-1]:
            self.nums[-1] = val
            self.nums = list(reversed(sorted(self.nums)))
        # print(self.nums)
        return self.nums[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
