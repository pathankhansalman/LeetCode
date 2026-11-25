class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        sum_arr = [arr[0]]
        sums = arr[0]
        for i in range(1, len(arr)):
            sums += arr[i]
            sum_arr.append(sums)
        found = 0
        tot_sum = sum(arr)
        #print(tot_sum/3.0, 2*tot_sum/3.0)
        for i in range(len(sum_arr) - 1):
            if found == 0 and sum_arr[i] == tot_sum/3.0:
                found = 1
            elif found == 1 and sum_arr[i] == 2*tot_sum/3.0:
                found = 2
        return found == 2
