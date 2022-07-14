from typing import List

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            if sum > target:
                right -= 1
            else:
                left += 1
