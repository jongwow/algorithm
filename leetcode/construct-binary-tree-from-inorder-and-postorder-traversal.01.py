from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verification(node: Optional[TreeNode]):
    if node == None:
        return []

    def inOrder(node: TreeNode):
        if node == None:
            return
        inOrder(node.left)
        print(node.val, end=' ')
        inOrder(node.right)

    def preOrder(node: TreeNode):
        if node == None:
            return
        print(node.val, end=' ')
        preOrder(node.left)
        preOrder(node.right)

    print('PreOrder: ', end='')
    preOrder(node)
    print()
    print('inOrder: ', end='')
    inOrder(node)
    print()


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        print(inorder, postorder)
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        if len(inorder) == 0:
            return None
        rootNodeValue = postorder[-1]
        rootNodeIndex = inorder.index(rootNodeValue)
        leftNode = self.buildTree(
            inorder[:rootNodeIndex], postorder[:rootNodeIndex])
        rightNode = self.buildTree(
            inorder[rootNodeIndex+1:], postorder[rootNodeIndex:-1])
        rootNode = TreeNode(postorder[-1])
        rootNode.left = leftNode
        rootNode.right = rightNode
        return rootNode


ans = Solution().buildTree([-1], [-1])
ans = Solution().buildTree([1, 2, 3, 4], [4, 3, 2, 1])
# ans = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
verification(ans)
