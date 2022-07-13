from typing import List

class Solution:
    """
    URL: https://leetcode.com/problems/two-sum/
    Time Complexity: O(n)
    Space Complexity: O(n)
    Hint: Use a hashset to store the numbers. If the difference from target is already in the hashset, return both indices.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
