import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        mod_para = paragraph
        syms = ["!", "?", "'", ",", ";", "."]
        for sym in syms:
            mod_para = mod_para.replace(sym, " ")
            mod_para = re.sub('[\s+]', ' ', mod_para)
            mod_para = mod_para.strip()
        mod_para = mod_para.lower().split(" ")
        word_count = {}
        for word in mod_para:
            if word == "":
                continue
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
        word_count = [(k, v) for k, v in word_count.items()]
        word_count = [x[0] for x in list(reversed(sorted(word_count, key=lambda x: x[1]))) if x[0] not in set(banned)]
        return word_count[0]
