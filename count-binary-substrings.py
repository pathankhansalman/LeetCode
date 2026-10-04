class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def count_helper(arg):
            stack = []
            start_char = s[0]
            idx = 0
            flipped_already = False
            count = 0
            while idx < len(s):
                #print(stack, flipped_already, start_char)
                if s[idx] == start_char and flipped_already:
                    count += min(sum(stack), len(stack) - sum(stack))
                    flipped_already = False
                    while stack[0] == int(start_char):
                        stack = stack[1:]
                    start_char = str(abs(1 - int(start_char)))
                if s[idx] != start_char:
                    flipped_already = True
                stack.append(int(s[idx]))
                idx += 1
                if idx == len(s):
                    if flipped_already:
                        count += min(sum(stack), len(stack) - sum(stack))
                    stack = []
                    break
            return count, stack
        if len(s) == 1:
            return 0
        full_count = 0
        curr_s = s
        while 1:
            count, stack = count_helper(curr_s)
            full_count += count
            if not stack or count == 0:
                break
            curr_s = ''.join(stack)
        return full_count
