class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        trans_sentence = []
        words = sentence.split(" ")
        inc = "a"
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        for word in words:
            if word[0] in vowels:
                curr_word = word + "ma"
            else:
                curr_word = word[1:] + word[0] + "ma"
            curr_word += inc
            trans_sentence.append(curr_word)
            inc += "a"
        return " ".join(trans_sentence)