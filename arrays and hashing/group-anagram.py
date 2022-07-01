from collections import defaultdict
from typing import List

class Solution:
    """
    URL: https://leetcode.com/problems/group-anagrams/
    Time Complexity: O(n)
    Space Complexity: O(n)
    Hint: sort each string and use it as a key for the hashmap and the string as the value. Then return the values of the hashmap. 
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            t = list(s)
            t.sort()
            t = "".join(t)
            res[t].append(s)
        return res.values()

    """
        Time Complexity: O(n*m) where n is the number of strings and m is the length of the longest string
        Space Complexity: O(n)
        Hint: Use a hashmap to store count of each character in each string. Use the count as key and append string to the value list. Then return the values of the hashmap.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()
