import heapq
from typing import List

"""
Time Complexity: O(nlog(n))
Space Complexity: O(n)
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x-0)**2) + (abs(y-0)**2)
            pts.append((dist, x, y))

        heapq.heapify(pts)
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])

        return res