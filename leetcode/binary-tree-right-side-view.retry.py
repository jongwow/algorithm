from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideViewV1(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = []
        result = []
        queue.append((root, 1))
        prev_height = 1
        prev_value = root.val
        while len(queue) != 0:
            current = queue.pop(0)
            if prev_height != current[1]:
                result.append(prev_value)
            if current[0].left is not None:
                queue.append((current[0].left, current[1]+1))
            if current[0].right is not None:
                queue.append((current[0].right, current[1]+1))
            prev_height = current[1]
            prev_value = current[0].val
        result.append(prev_value)
        return result

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []

        def nextLevel(node: Optional[TreeNode], level: int):
            if node is None:
                return
            if len(result) == level:
                result.append(node.val)
            nextLevel(node.right, level+1)
            nextLevel(node.left, level+1)
        nextLevel(root, 0)
        return result


tcs = [
    TreeNode(1, TreeNode(2, None, TreeNode(5)),
             TreeNode(3, None, TreeNode(4))),
    TreeNode(1, None, TreeNode(3)),
    None
]


def levelOrder(node):  # like bfs
    if node is None:
        return
    queue = []
    queue.append(node)
    while len(queue) != 0:
        current = queue.pop(0)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
        print(current.val)


for tc in tcs:
    # levelOrder(tc)
    sol = Solution().rightSideView(tc)
    print(sol)
