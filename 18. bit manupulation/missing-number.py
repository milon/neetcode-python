from typing import List

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for i in range(1, len(nums)+1):
            missing ^= i
        for num in nums:
            missing ^= num
        return missing
