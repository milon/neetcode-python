from typing import List

"""
Time Complexity: O(nlog(n))
Space Complexity: O(n)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        count = dict(sorted(count.items(), key=lambda item: -item[1]))
        return list(count.keys())[:k]
