import collections
import heapq
from typing import List

"""
Time Complexity, O(E*logV), E is the number of edges, V is the number of vertices.
Space Complexity, O(V+E)
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for s, d, w in times:
            graph[s].append((d, w))

        minHeap = [(0, k)]
        visit = set()
        time = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue

            visit.add(n1)
            time = max(time, w1)

            for n2, w2 in graph[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))

        return time if len(visit) == n else -1
