# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:09:22 2022

@author: patha
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = prices[0]
        sell_price = prices[0]
        curr_buy_price = prices[0]
        curr_sell_price = prices[0]
        max_profit = 0
        inc = False
        for i in range(1, len(prices)):
            if prices[i] >= curr_sell_price:
                if not inc:
                    inc = True
                curr_sell_price = prices[i]
                if curr_sell_price - curr_buy_price > max_profit:
                    max_profit = (curr_sell_price - curr_buy_price)
            elif prices[i] < curr_buy_price:
                curr_sell_price = prices[i]
                curr_buy_price = prices[i]
            elif prices[i] < curr_sell_price:
                if inc:
                    if curr_sell_price - curr_buy_price > max_profit:
                        max_profit = (curr_sell_price - curr_buy_price)
                curr_sell_price = prices[i]
        return max_profit