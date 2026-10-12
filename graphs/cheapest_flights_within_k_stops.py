# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:11:33 2026

@author: patha
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # Initialize the cost array with infinity
        prices = [float('inf')] * n
        prices[src] = 0
        
        # Iterate at most K + 1 times (K stops means at most K + 1 edges)
        for _ in range(k + 1):
            # Create a snapshot copy of current prices to prevent updating 
            # and using the same edge within the same iteration loop
            temp_prices = prices[:]
            
            for u, v, price in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + price < temp_prices[v]:
                    temp_prices[v] = prices[u] + price
            
            prices = temp_prices
            
        return prices[dst] if prices[dst] != float('inf') else -1

# Example Execution
if __name__ == "__main__":
    sol = Solution()
    # flights = [[source, destination, price]]
    flight_network = [[0,1,100],[1,2,100],[0,2,500],[1,3,600],[2,3,200]]
    
    print(f"Cheapest path within 1 stop: {sol.findCheapestPrice(4, flight_network, 0, 3, 1)}") # Output: 700 (0 -> 1 -> 3)
