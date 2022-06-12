# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 12:09:18 2022

@author: patha
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_dict = {k: [] for k in range(numCourses)}
        root_dict = {k: True for k in range(numCourses)}
        for prereq in prerequisites:
            if prereq[0] == prereq[1]:
                return False
            adj_dict[prereq[0]].append(prereq[1])
            root_dict[prereq[1]] = False
        if not any(root_dict.values()):
            return False
        roots = [k for k in root_dict.keys() if root_dict[k]]
        # print(roots)
        for root in root_dict.keys():
            curr_path = [root]
            curr_exp = set([root])
            master_exp = set([root])
            reset = True
            while len(curr_path) > 0:
                if reset:
                    curr_start = curr_path[-1]
                    next_exp_list = [x for x in adj_dict[curr_start] if x not in master_exp]
                    reset = False
                child_found = False
                for i, node in enumerate(next_exp_list):
                    child_list = adj_dict[node]
                    # print(child_list, curr_exp)
                    if any([x in curr_exp for x in child_list]):
                        return False
                    curr_exp.add(node)
                    master_exp.add(node)
                    curr_path.append(node)
                    if len(child_list) == 0:
                        break
                    if len(child_list) > 0:
                        child_found = True
                        next_exp_list = [x for x in next_exp_list[i + 1:] if x not in child_list]
                        next_exp_list = child_list + next_exp_list
                        break
                if child_found:
                    continue
                # print(curr_path)
                curr_exp.remove(curr_path[-1])
                curr_path = curr_path[:-1]
                reset = True
        return True