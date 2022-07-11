from typing import List

"""
Time Complexity: O(n*m)
Space Complexity: O(n*m)
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r, c) in visit:
                return 0
            visit.add((r, c))
            land = 1
            land += dfs(r-1, c)
            land += dfs(r+1, c)
            land += dfs(r, c-1)
            land += dfs(r, c+1)
            return land

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
