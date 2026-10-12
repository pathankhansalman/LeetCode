class Solution(object):
    def myAtoi(self, s):
        retval = s.strip()
        if not retval:
            return 0
        mul = 1
        if retval[0] in ['+', '-']:
            if retval[0] == '-':
                mul = -1
            retval = retval[1:]
        elif retval[0] not in [str(x) for x in range(10)]:
            return 0
        if not retval:
            return 0
        i = None
        for idx in range(len(retval)):
            if retval[idx] not in [str(x) for x in range(10)]:
                i = idx
                break
        if i == 0:
            return 0
        retval = mul*int(retval[:i])
        if retval < -2**31:
            return -2**31
        elif retval > 2**31 - 1:
            return 2**31 - 1
        return retval


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi('42'))
    print(s.myAtoi('     -42'))
    print(s.myAtoi('4193 with words'))
    print(s.myAtoi('words and 987'))
    print(s.myAtoi('-91283472332'))
    print(s.myAtoi('+-12'))
    print(s.myAtoi('   +0 123'))
