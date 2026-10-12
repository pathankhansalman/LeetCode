class TreeNode:
    def __init__(self, val=0, left_index=0, right_index=0):
        self.val = val
        self.left_index = left_index
        self.right_index = right_index
        self.left = None
        self.right = None

class NumArray:

    def __init__(self, nums: List[int]):
        def _tree_helper_(left, right):
            if right == left:
                return TreeNode(nums[right], left, right)
            elif right - left == 1:
                left_child = TreeNode(nums[left], left, left)
                right_child = TreeNode(nums[right], right, right)
                retval = TreeNode(nums[left] + nums[right], left, right)
                retval.left = left_child
                retval.right = right_child
                return retval
            else:
                mid = (right + left) // 2
                left_child = _tree_helper_(left, mid)
                right_child = _tree_helper_(mid + 1, right)
                retval = TreeNode(left_child.val + right_child.val, left, right)
                retval.left = left_child
                retval.right = right_child
                return retval
        self.tree = _tree_helper_(0, len(nums) - 1)
        self.nums = nums
        

    def update(self, index: int, val: int) -> None:
        def _up_tree_(arg):
            if arg is None:
                return None
            if index >= arg.left_index and index <= arg.right_index:
                arg.val += (val - self.nums[index])
                _up_tree_(arg.left)
                _up_tree_(arg.right)
        _up_tree_(self.tree)
        self.nums[index] = val
        return None
        
        

    def sumRange(self, left: int, right: int) -> int:
        def _get_sum_(arg, arg1, arg2):
            if arg is None:
                return 0
            if arg1 == arg.left_index and arg2 == arg.right_index:
                return arg.val
            mid = (arg.left_index + arg.right_index) // 2
            if arg2 <= mid:
                return _get_sum_(arg.left, arg1, arg2)
            elif arg1 > mid:
                return _get_sum_(arg.right, arg1, arg2)
            else:
                return _get_sum_(arg.left, arg1, mid) + _get_sum_(arg.right, mid + 1, arg2)
        return _get_sum_(self.tree, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)