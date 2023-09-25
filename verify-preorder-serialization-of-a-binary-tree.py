class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder == "#":
            return True
        if len(preorder) == 1:
            return False
        if preorder[0] == "#":
            return False
        check_s = preorder.split(",")
        count = 0
        num_count = 0
        for char in check_s:
            if char == "#":
                count += 1
            else:
                num_count += 1
            if count > num_count + 1:
                return False
        if count > (len(check_s) //2) + 1:
            return False
        s = preorder
        length = len(s)
        curr_len = 0
        while 1:
            print(s)
            if s == "#":
                return True
            if length == curr_len:
                return False
            idx = s.find("#,#")
            if idx == -1:
                return False
            length = len(s)
            bef_comma = s[:idx-1].rfind(",")
            s = s[:bef_comma+1] + "#" + s[idx+3:]
            curr_len = len(s)
