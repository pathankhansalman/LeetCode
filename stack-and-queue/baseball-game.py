import numpy as np

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        retval = []
        for op in operations:
            if op.isdigit():
                retval.append(int(op))
            elif op[0] == "-" and op[1:].isdigit():
                retval.append(int(op))
            elif op == "+":
                retval.append(retval[-1] + retval[-2])
            elif op == "D":
                retval.append(2*retval[-1])
            elif op == "C":
                retval = retval[:-1]
        return int(np.sum(retval))
