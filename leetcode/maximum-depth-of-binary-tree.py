from typing import List, Optional
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1
        que = deque([(root, 1)])
        while que:
            cu = que.popleft()
            depth = cu[1]
            if cu[0].left:
                que.append((cu[0].left, cu[1]+1))
            if cu[0].right:
                que.append((cu[0].right, cu[1]+1))
        return depth

    def maxDepthV3(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1
        que = [(root, 1)]
        while len(que) != 0:
            cu = que.pop(0)
            depth = cu[1]
            if cu[0].left:
                que.append((cu[0].left, cu[1]+1))
            if cu[0].right:
                que.append((cu[0].right, cu[1]+1))
        return depth

    def maxDepthV2(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            current = 1
            left = current + self.maxDepth(root.left)
            right = current + self.maxDepth(root.right)
            return max(current, left, right)

    def maxDepthV1(self, root: Optional[TreeNode]) -> int:
        if root == None:
            # print('getDepth: Hit')
            return 0
        else:
            current = 1
            left = 1 + self.getDepth(root.left)
            right = 1 + self.getDepth(root.right)
            res = max(current, left, right)
            # print('getDepth of ', root.val, 'is ', res)
            return res


t1 = TreeNode(3)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)
t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5


sol = Solution().maxDepth(t1)
print(sol)
# X = 1
# Y = 0
# distMap = [[0 for j in range(M)] for i in range(N)]
# visitedMap = [[0 for j in range(M)] for i in range(N)]
# Q = []
# Q.append((cY, cX))
# result = 55
# while len(Q) != 0:
#     pos = Q.pop(0)
#     if seaMap[pos[Y]][pos[X]] == 1:
#         return distMap[pos[Y]][pos[X]]
#     for dir in dirs:
#         nY = pos[Y] + dir[Y]
#         nX = pos[X] + dir[X]
#         if boundary(N, M, nY, nX) and visitedMap[nY][nX] == 0:
#             visitedMap[nY][nX] = 1
#             distMap[nY][nX] = distMap[pos[Y]][pos[X]] + 1
#             Q.append((nY, nX))
# return result
