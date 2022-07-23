import heapq
from typing import List

"""
Time Complexity: O(n+klog(n)), where n is the length of nums, and k is the value of k.
Space Complexity: O(n)
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k > 0:
            item = heapq.heappop(nums)
            k -= 1
        return -item
