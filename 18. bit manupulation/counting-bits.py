from typing import List

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        msb = 1

        for i in range(1, n+1):
            if msb * 2 == i:
                msb = i
            dp[i] = 1 + dp[i-msb]
        return dp
