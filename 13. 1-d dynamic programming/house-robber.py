from typing import List

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        def countSum(i, memo):
            if i in memo:
                return memo[i]

            if i >= len(nums):
                return 0

            include = nums[i] + countSum(i+2, memo)
            exclude = countSum(i+1, memo)
            memo[i] = max(include, exclude)
            return memo[i]

        return countSum(0, {})
