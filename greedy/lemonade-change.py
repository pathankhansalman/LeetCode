class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count_dict = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                count_dict[5] += 1
            elif bill == 10:
                count_dict[10] += 1
                if count_dict[5] < 1:
                    return False
                count_dict[5] -= 1
            elif bill == 20:
                count_dict[20] += 1
                if count_dict[10] >= 1 and count_dict[5] >= 1:
                    count_dict[10] -= 1
                    count_dict[5] -= 1
                elif count_dict[5] >= 3:
                    count_dict[5] -= 3
                else:
                    return False
        return True