class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_dict = dict(zip(list(order), sorted(list(order))))
        mapped_words = [''.join(order_dict[char] for char in word) for word in words]
        return mapped_words == sorted(mapped_words)