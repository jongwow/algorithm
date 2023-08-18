from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
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
        print(values)
        return result


# t1 = TreeNode(4)
# t2 = TreeNode(2)
# t3 = TreeNode(6)
# t4 = TreeNode(1)
# t5 = TreeNode(3)
# t1.left = t2
# t1.right = t3
# t2.left = t4
# t2.right = t5


t1 = TreeNode(543)
t2 = TreeNode(384)
t3 = TreeNode(652)
t5 = TreeNode(445)
t7 = TreeNode(699)
t1.left = t2
t1.right = t3
t2.right = t5
t3.right = t7

sol = Solution().getMinimumDifference(t1)
print(sol)
