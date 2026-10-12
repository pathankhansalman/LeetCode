class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        mydict = {}
        for char in s:
            if char not in mydict:
                mydict[char] = 0
            mydict[char] += 1
        retval = ""
        for char in s:
            print(retval, mydict)
            idx = retval.find(char)
            if idx == -1:
                retval += char
                mydict[char] -= 1
                continue
            elif idx == len(retval) - 1:
                mydict[char] -= 1
                continue
            greater = True
            for tgt in retval[idx + 1:]:
                if ord(tgt) > ord(char):
                    if mydict[tgt] == 0:
                        greater = True
                        break
                if ord(tgt) < ord(char):
                    greater = False
                    break
            if greater:
                mydict[char] -= 1
                continue
            retval = retval[:idx] + retval[idx + 1:] + char
            mydict[char] -= 1
        return retval
