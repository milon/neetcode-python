"""
Time Complexity: O(1), as we always iterate 32 times.
Space Complexity: O(1)
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
        return res
