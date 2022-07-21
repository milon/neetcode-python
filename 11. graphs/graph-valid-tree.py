from typing import List

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        graph = {i: [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
