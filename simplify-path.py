# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 23:20:14 2022

@author: patha
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if len(path) == 1:
            return path
        mystr = path
        prev_len = len(mystr)
        while 1:
            mystr = mystr.replace('//', '/')
            curr_len = len(mystr)
            if curr_len == prev_len:
                break
            prev_len = len(mystr)
        if len(mystr) == 1:
            return mystr
        if mystr[0] == '/':
            mystr = mystr[1:]
        if mystr[-1] == '/':
            mystr = mystr[:-1]
        comps = mystr.split('/')
        new_path = ['/']
        for comp in comps:
            if comp == '.':
                continue
            if comp == '..':
                if new_path == ['/']:
                    continue
                new_path[:] = new_path[:-1]
            else:
                new_path.append(comp + '/')
        new_path = ''.join(new_path)
        if len(new_path) == 1:
            return new_path
        return new_path[:-1]