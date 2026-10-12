class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        num_lines = 1
        lines = []
        num_pixels = 0
        curr_line = ''
        for char in s:
            if num_pixels + widths[ord(char) - ord('a')] > 100:
                num_lines += 1
                lines.append(curr_line)
                num_pixels = 0
                curr_line = ''
            curr_line += char
            num_pixels += widths[ord(char) - ord('a')]
        return [num_lines, num_pixels]
