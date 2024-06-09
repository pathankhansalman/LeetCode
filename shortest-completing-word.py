class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def _get_char_dict_(arg):
            retval = {}
            for char in arg:
                if char.isdigit():
                    continue
                if char == " ":
                    continue
                if char.lower() not in retval:
                    retval[char.lower()] = 0
                retval[char.lower()] += 1
            return retval
        def _is_complete_(arg1, arg2):
            for key in arg1.keys():
                if key not in arg2:
                    return False
                if arg1[key] > arg2[key]:
                    return False
            return True
        completes = {}
        for word in words:
            if _is_complete_(_get_char_dict_(licensePlate), _get_char_dict_(word)):
                completes[word] = 1
        if len(completes.keys()) == 1:
            return list(completes.keys())[0]
        else:
            completes = [word for word in completes if len(word) == min([len(x) for x in completes])]
            for word in words:
                if word in completes:
                    return word
