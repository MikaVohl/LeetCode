from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(current, depth):
            if current == None:
                return depth
            return max(traverse(current.left, depth + 1), traverse(current.right, depth + 1))

        return traverse(root, 0)