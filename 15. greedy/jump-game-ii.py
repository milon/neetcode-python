from typing import List

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        res = 0
        while right < len(nums)-1:
            max_jump = 0
            for i in range(left, right+1):
                max_jump = max(max_jump, i+nums[i])
            left = right+1
            right = max_jump
            res += 1
        return res
