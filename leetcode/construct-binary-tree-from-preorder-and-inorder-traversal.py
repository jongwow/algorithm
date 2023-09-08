from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# preOrder => 나, 왼쪽, 오른쪽
# inOrder => 왼쪽, 나, 오른쪽
# postOrder => 왼쪽, 오른쪽, 나


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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        if len(preorder) == 0:
            return None
        rootVal = preorder[0]
        rootIndex = inorder.index(rootVal)
        leftInorder = inorder[0:rootIndex]
        leftPreOrder = preorder[1:1+len(leftInorder)]
        leftNode = self.buildTree(leftPreOrder, leftInorder)
        rightInorder = inorder[rootIndex+1:len(inorder)]
        rightPreorder = preorder[1+len(leftPreOrder):]
        rightNode = self.buildTree(rightPreorder, rightInorder)
        rootNode = TreeNode(rootVal)
        rootNode.left = leftNode
        rootNode.right = rightNode
        return rootNode


tcs = [
    [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]]
]
for tc in tcs:
    sol = Solution().buildTree(tc[0], tc[1])
    verification(sol)
    # print(sol)
