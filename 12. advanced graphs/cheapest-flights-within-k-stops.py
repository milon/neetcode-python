import math
from typing import List

"""
Time Complexity: O(n*k), n is the number of vertices, k is the number of stops.
Space Complexity: O(n)
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0

        for i in range(k+1):
            tempPrices = prices.copy()

            for s, d, p in flights:
                if prices[s] == math.inf:
                    continue
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p
            prices = tempPrices

        return -1 if prices[dst] == math.inf else prices[dst]
