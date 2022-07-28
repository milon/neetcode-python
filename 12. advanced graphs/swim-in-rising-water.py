import heapq
from typing import List

"""
Time Complexity: O(n^2 * log(n)), n is the number of elements in the grid.
Space Complexity: O(n)
"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visit.add((0, 0))
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return time
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (
                    row < 0
                    or col < 0
                    or row >= N
                    or col >= N
                    or (row, col) in visit
                ):
                    continue

                visit.add((row, col))
                heapq.heappush(minHeap, (max(time, grid[row][col]), row, col))
