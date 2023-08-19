from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        values = []
        while len(queue) != 0:
            current = queue.pop(0)
            values.append(current.val)
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
        result = 10000000
        values.sort()
        for n in range(1, len(values)):
            gap = abs(values[n] - values[n-1])
            result = min(gap, result)
        return result
