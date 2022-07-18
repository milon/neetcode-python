from typing import List

"""
Time Complexity: O(n), where n is the length of the array.
Space Complexity: O(1)
"""

class Solution:
    def encode(self, s: List[str]) -> str:
        return '$$'.join(s)

    def decode(self, s: str) -> List[str]:
        return s.split('$$')