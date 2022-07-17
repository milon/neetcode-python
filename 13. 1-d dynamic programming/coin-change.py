from typing import List

"""
Time Complexity: O(n*a), n is the number of coins, a is the amount of money
Space Complexity: O(n*a)
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoin = self._coinChange(coins, amount, {})
        return minCoin if minCoin != float("inf") else -1

    def _coinChange(self, coins: List[int], amount: int, memo: dict) -> int:
        if amount in memo:
            return memo[amount]

        if amount < 0:
            return float("inf")
        if amount == 0:
            return 0

        minCoin = float("inf")
        for coin in coins:
            minCoin = min(minCoin, self._coinChange(coins, amount-coin, memo))
        memo[amount] = 1+minCoin
        return memo[amount]
