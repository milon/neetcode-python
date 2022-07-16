from typing import List

"""
Time Complexity: O(n+p), where n is the number of courses and p is the number prerequisites.
Space Complexity: O(n+p)
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.buildGraph(numCourses, prerequisites)
        visited, visiting = set(), set()
        res = []

        def hasCycle(node):
            if node in visiting:
                return True
            if node in visited:
                return False
            visiting.add(node)
            for neighbor in graph[node]:
                if hasCycle(neighbor):
                    return True
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return False

        for course in range(numCourses):
            if hasCycle(course):
                return []
        return res

    def buildGraph(self, numCourses, prerequisites):
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for a, b in prerequisites:
            graph[a].append(b)
        return graph
