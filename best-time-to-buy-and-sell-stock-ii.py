# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:09:07 2022

@author: patha
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curr_buy_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= curr_buy_price:
                max_profit += (prices[i] - curr_buy_price)
                curr_buy_price = prices[i]
            elif prices[i] < curr_buy_price:
                curr_buy_price = prices[i]
        return max_profit