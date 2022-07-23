from typing import List

"""
Time Complexity: O(2^n)
Space Complexity: O(n), as we store directly to the result array, which doesn't count as extra space.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(index: int) -> None:
            if index >= len(nums):
                res.append(subset.copy())
                return

            # include nums[index]
            subset.append(nums[index])
            backtrack(index+1)

            # exclude nums[index]
            subset.pop()
            backtrack(index+1)

        backtrack(0)
        return res
