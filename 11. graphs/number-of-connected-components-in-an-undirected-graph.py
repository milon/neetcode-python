from typing import List

"""
Time Complexity: O(n*e), n is the number of nodes, and e is the number of edges.
Space Complexity: O(n*e)
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()
        count = 0

        def dfs(node) -> bool:
            if node in visited:
                return False
            visited.add(node)
            for n in graph[node]:
                dfs(n)
            return True
        
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        
        return count