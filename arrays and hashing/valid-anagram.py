class Solution:
    """
    URL: https://leetcode.com/problems/valid-anagram/
    Time Complexity: O(nlog(n))
    Space Complexity: O(1)
    Hint: Sort the strings and compare them.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        
        s = list(s)
        t = list(t)

        s.sort()
        t.sort()        
        
        for i in range(len(s)):
            if s[i] != t[i]: return False
            
        return True