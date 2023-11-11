from typing import List, Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        firstQueue = deque([root])
        queue = deque([firstQueue])
        while len(queue) > 0:
            currentQueue = queue.popleft()
            nextQueue = deque([])
            ansans = []
            while len(currentQueue) > 0:
                current = currentQueue.popleft()
                # print("current:", current.val)
                ansans.append(current.val)
                if current.left:
                    nextQueue.append(current.left)
                if current.right:
                    nextQueue.append(current.right)
            if len(nextQueue) > 0:
                queue.append(nextQueue)
            if len(ansans) > 0:
                ans.append(ansans)
        return ans

    def levelOrderV1(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque([root])
        while len(queue) > 0:
            current = queue.popleft()
            ans.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return ans


root1 = TreeNode(3, TreeNode(9, None, None),
                 TreeNode(20, TreeNode(15), TreeNode(7)))
root2 = None
root3 = TreeNode(1)
ans = Solution().levelOrder(root1)
print(ans)

ans = Solution().levelOrder(root2)
print(ans)

ans = Solution().levelOrder(root3)
print(ans)
