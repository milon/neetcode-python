from typing import List

"""
Time Complexity: O(n+p), where n is the number of courses and p is the number prerequisites.
Space Complexity: O(n+p)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses, prerequisites)
        visiting, visited = set(), set()

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
            return False

        for course in range(numCourses):
            if hasCycle(course):
                return False
        return True

    def buildGraph(self, numCourses, prerequisites):
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for a, b in prerequisites:
            graph[a].append(b)
        return graph
