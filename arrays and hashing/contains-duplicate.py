from typing import List

class Solution:
    """
    URL: https://leetcode.com/problems/contains-duplicate/
    Time Complexity: O(n)
    Space Complexity: O(n)
    Hint: Use a hashset to store the numbers. If the number is already in the hashset, return True.
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False