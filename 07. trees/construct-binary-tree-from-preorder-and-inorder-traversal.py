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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMapping = {}
        for k, v in enumerate(inorder):
            inorderMapping[v] = k

        index = 0

        def treeBuilder(left, right):
            nonlocal index
            if left > right:
                return None
            rootVal = preorder[index]
            root = TreeNode(rootVal)
            index += 1
            root.left = treeBuilder(left, inorderMapping[rootVal]-1)
            root.right = treeBuilder(inorderMapping[rootVal]+1, right)
            return root

        return treeBuilder(0, len(preorder)-1)
