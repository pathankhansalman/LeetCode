class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 1
        j = 1
        name_stack = [name[0]]
        typed_stack = [typed[0]]
        while i < len(name) and j < len(typed):
            print(i, j, name[i], typed[j], name_stack, typed_stack)
            if name[i] == typed[j]:
                if name[i] == name_stack[-1] and typed[j] == typed_stack[-1]:
                    name_stack.append(name[i])
                    typed_stack.append(typed[j])
                    i += 1
                    j += 1
                    continue
                else:
                    if len(name_stack) <= len(typed_stack):
                        name_stack = [name[i]]
                        typed_stack = [typed[j]]
                        i += 1
                        j += 1
                        continue
                    return False
            if name[i] != typed[j]:
                if len(name_stack) <= len(typed_stack):
                    if name[i] == name_stack[-1]:
                        name_stack.append(name[i])
                        i += 1
                        continue
                    if typed[j] == typed_stack[-1]:
                        typed_stack.append(typed[j])
                        j += 1
                        continue
                    return False
                return False
        name_last = ''.join(name_stack) + name[i:]
        typed_last = ''.join(typed_stack) + typed[j:]
        print(name_last, typed_last)
        if set(list(name_last)) == set(list(typed_last)) and len(set(list(name_last))) == 1:
            return True
        return False