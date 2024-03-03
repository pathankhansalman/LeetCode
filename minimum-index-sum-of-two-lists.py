class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {list1[i]: i for i in range(len(list1))}
        dict2 = {list2[i]: i for i in range(len(list2))}
        list_in = list(set(list1).intersection(set(list2)))
        in_dict = {}
        min_idx = 1000000000
        for item in list_in:
            in_dict[item] = dict1[item] + dict2[item]
            if dict1[item] + dict2[item] < min_idx:
                min_idx = dict1[item] + dict2[item]
        return [k for k in list_in if in_dict[k] == min_idx]
