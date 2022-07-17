from typing import List

"""
Time Complexity: O(n*t), n is the number of elements in the array, t is the target sum
Space Complexity: O(n*t)
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def findWays(index, current_sum, memo):
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            if index < 0 and current_sum == target:
                return 1
            if index < 0:
                return 0

            positive = findWays(index-1, current_sum+nums[index], memo)
            negative = findWays(index-1, current_sum-nums[index], memo)
            memo[(index, current_sum)] = positive + negative

            return memo[(index, current_sum)]

        index = len(nums)-1
        return findWays(index, 0, {})
