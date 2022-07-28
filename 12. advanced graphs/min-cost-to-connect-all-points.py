import heapq
from typing import List

"""
Time Complexity: O(n^2 * log(n)), n is the number of vertices.
Space Complexity: O(n)
"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        graph = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                graph[i].append([dist, j])
                graph[j].append([dist, i])

        # Prims' algorithm
        res = 0
        visited = set()
        minHeap = [[0, 0]]
        while len(visited) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in graph[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])

        return res
