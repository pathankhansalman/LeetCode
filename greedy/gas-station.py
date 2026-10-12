# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:50:40 2022

@author: patha
"""

import numpy as np
from copy import deepcopy
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if np.sum(cost) > np.sum(gas):
            return -1
        start_idx = False
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                if cost[i] == 0 and gas[i] == 0:
                    continue
                start_idx = True
                break
        if not start_idx:
            return -1
        surp_req = [0 for x in gas]
        start_idx = len(gas) - 1
        curr_idx = start_idx
        curr_gas = 0
        min_curr_gas = 999999999999
        while 1:
            curr_gas += gas[curr_idx]
            curr_gas -= cost[curr_idx]
            curr_idx += 1
            curr_idx %= len(gas)
            # print(curr_idx, curr_gas)
            if curr_gas < min_curr_gas:
                min_curr_gas = curr_gas
            if curr_idx == start_idx:
                break
        if min_curr_gas >= 0:
            return start_idx
        surp_req[-1] = min_curr_gas
        for i in range(len(gas) - 2, -1, -1):
            surp_req[i] = surp_req[i + 1] - cost[i] + gas[i]
            if surp_req[i] >= 0:
                return i
        return -1