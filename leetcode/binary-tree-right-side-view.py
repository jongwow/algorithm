from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            result = []
            elem = (root, 1)
            queue = [elem]
            while len(queue) != 0:
                cur = queue.pop(0)
                print('cur: ', cur[0].val)
                if cur[1] != elem[1]:
                    print('boom: ', elem[0].val)
                    result.append(elem[0].val)
                if cur[0].left != None:
                    queue.append((cur[0].left, cur[1] + 1))
                if cur[0].right != None:
                    queue.append((cur[0].right, cur[1] + 1))
                elem = cur
            result.append(elem[0].val)
            return result

    def rightSideView_wrong(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            res = [root.val]
            next = self.rightSideView(root.right)
            return res + next


# === Test Case 1 ===#
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(5)
t5 = TreeNode(4)
t1.left = t2
t1.right = t3
t2.right = t4
t3.right = t5

# === Test Case 2 ===#
# t1 = TreeNode(1)
# t2 = TreeNode(3)
# t1.right = t2

# === Test Case 3 ===#
# t1 = None

# === Test Case 4 ===#
# t1 = TreeNode(1)
# t2 = TreeNode(2)
# t1.left = t2

sol = Solution().rightSideView(t1)

print(sol)
