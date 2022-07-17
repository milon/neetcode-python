"""
Time Complexity: O(n*m)
space Complexity: O(n*m)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def findPaths(r, c, memo):
            if (r, c) in memo:
                return memo[(r, c)]
            if r >= m or c >= n:
                return 0
            if r == m-1 and c == n-1:
                return 1
            memo[(r, c)] = findPaths(r+1, c, memo) + findPaths(r, c+1, memo)
            return memo[(r, c)]

        return findPaths(0, 0, {})
