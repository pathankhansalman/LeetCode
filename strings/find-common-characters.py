class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        char_dict = {}
        trav_dict = {}
        for word in words:
            trav_dict = {k: False for k in trav_dict.keys()}
            for char in word:
                if trav_dict.get(char, False):
                    continue
                if char not in char_dict:
                    char_dict[char] = 0
                char_dict[char] += 1
                trav_dict[char] = True
        uniq_list = [k for k in char_dict.keys() if char_dict[k] == len(words)]
        retval = []
        for uniq_char in uniq_list:
            retval += [uniq_char]*min([word.count(uniq_char) for word in words])
        return retval
