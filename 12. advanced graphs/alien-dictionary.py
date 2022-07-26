from typing import List

"""
Time Complexity: O(n), n is the number of characters combined in the input array.
Space Complexity: O(n)
"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = self.createGraph(words)
        return self.topologicalSort(graph)

    def topologicalSort(self, graph: List[List[str]]) -> str:
        visited = set()
        result = []
        for node in graph:
            if node not in visited:
                self.dfs(node, graph, visited, result)
        return "".join(result)

    def dfs(self, node, graph, visited, result):
        if node in visited:
            return
        visited.add(node)
        for n in graph[node]:
            self.dfs(n, graph, visited, result)
        result.append(node)

    def createGraph(self, words: List[str]) -> List[List[str]]:
        graph = {}
        for word in words:
            for char in word:
                graph[char] = set()
        
        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    graph[words[i][j]].add(words[i+1][j])
                    break
        return graph

# s = Solution()
# print(s.alienOrder(["wrt","wrf","er","ett","rftt"]))