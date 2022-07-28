import collections
from typing import List

"""
Time Complexity: O(E^2), E is the number of edges.
Space Complexity: O(E)
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {s: collections.deque() for s, d in tickets}
        res = ["JFK"]

        tickets.sort()
        for s, d in tickets:
            graph[s].append(d)

        def dfs(cur):
            if len(res) == len(tickets)+1:
                return True
            if cur not in graph:
                return False

            temp = list(graph[cur])
            for d in temp:
                graph[cur].popleft()
                res.append(d)
                if dfs(d):
                    return res
                res.pop()
                graph[cur].append(d)
            return False

        dfs("JFK")
        return res
