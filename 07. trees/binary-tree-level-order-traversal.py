import collections
from typing import List, Optional

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.appendleft(root)
        while q:
            curLevelCount = len(q)
            currentLevelVal = []
            for i in range(curLevelCount):
                current = q.pop()
                currentLevelVal.append(current.val)
                if current.left:
                    q.appendleft(current.left)
                if current.right:
                    q.appendleft(current.right)
            res.append(currentLevelVal)
        return res
