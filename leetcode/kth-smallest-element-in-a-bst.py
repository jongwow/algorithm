from typing import Optional
# Definition for a binary tree node.

# 0005 ~ 0012


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def inOrder(root: Optional[TreeNode]):
            if root == None:
                return
            inOrder(root.left)
            result.append(root.val)
            if len(result) == k:
                return root.val
            inOrder(root.right)
        inOrder(root)
        return result[k-1]
