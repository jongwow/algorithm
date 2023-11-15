from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#  [5,4,6,null,null,3,7]
a = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.isValidBSTWithValue(root, None, None)

    def isValidBSTWithValue(self, root: Optional[TreeNode], bottom=None, upper=None) -> bool:
        if root == None:
            return True
        if bottom != None and root.val <= bottom:
            return False
        if upper != None and root.val >= upper:
            return False
        isLeft = True
        if root.left != None:
            isLeft = root.val > root.left.val and self.isValidBSTWithValue(
                root.left, bottom, root.val)
        isRight = True
        if root.right != None:
            isRight = root.val < root.right.val and self.isValidBSTWithValue(
                root.right, root.val, upper)
        return isLeft and isRight

        # left에 대해서 검증할 땐, leftNode에 있는 모든 값들은 root.val보다 작아야함.
        # - 아래 노드들 입장에선 위로부터 내려온 leftValue 보다 작아야함
        # right 에 대해서 검증할 때는, rightNode에 있는 모든 값들은 root.val 보다 커야함.


ans = Solution().isValidBST(a)
print(ans)
