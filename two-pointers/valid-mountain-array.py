class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        i = 0
        j = len(arr) - 1
        steps = 0
        while i < j and steps < len(arr):
            if arr[i + 1] == arr[i] or arr[j - 1] == arr[j]:
                return False
            if arr[i + 1] > arr[i]:
                i += 1
            if arr[j - 1] > arr[j]:
                j -= 1
            steps += 1
        return (i == j and i != 0 and i != len(arr) - 1)