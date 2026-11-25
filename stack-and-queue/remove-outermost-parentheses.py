class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        components = []
        component = ""
        sum = 0
        for char in s:
            if char == "(":
                sum += 1
            else:
                sum -= 1
            component += char
            if sum == 0:
                components.append(component)
                component = ""
        return "".join([component[1:-1] for component in components])
