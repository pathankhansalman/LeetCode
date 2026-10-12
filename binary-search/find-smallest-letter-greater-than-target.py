class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters_sort = list(sorted(letters, key=lambda x: ord(x)))
        for letter in letters_sort:
            if ord(letter) > ord(target):
                return letter
        return letters[0]