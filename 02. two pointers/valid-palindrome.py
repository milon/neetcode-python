"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            if not (s[left].isalpha() or s[left].isnumeric()):
                left += 1
            elif not (s[right].isalpha() or s[right].isnumeric()):
                right -= 1
            else:
                return False
        return True