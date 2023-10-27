from typing import Optional

"""
아직 완성되지 않은 코드입니다.

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def find(self, val):
        if (self.findNode(self.root, val) is False):
            return False
        return True

    def findNode(self, node, val):
        if node == None:
            return False
        if node.val == val:
            return True
        if node.val < val:
            return self.findNode(node.right, val)
        if node.val > val:
            return self.findNode(node.left, val)

    def insert(self, val):
        if (self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, node, val):
        if val <= node.val:
            if node.leftChild:
                self.insertNode(node.leftChild, val)
            else:
                node.leftChild = Node(val)
        elif val > node.val:
            if node.rightChild:
                self.insertNode(node.rightChild, val)
            else:
                node.rightChild = Node(val)

    def delete(self, val):
        self.deleteNode(self.root, val)

    def deleteNode(self, node: Optional[Node], val):
        parentNode = node
        currentNode = node
        parentNodeDirection = ''
        while currentNode.val != val:
            if currentNode.val < val:
                if currentNode.rightChild is None:
                    break
                else:
                    parentNode = currentNode
                    parentNodeDirection = 'right'
                    currentNode = currentNode.rightChild
            elif currentNode.val > val:
                if currentNode.leftChild is None:
                    break
                else:
                    parentNode = currentNode
                    parentNodeDirection = 'left'
                    currentNode = currentNode.leftChild
            # currentNode.val == val.. But already filtered by while condition
        if parentNode == currentNode:  # 고민중.
            assert False
        if currentNode.val == val:
            # case1
            if currentNode.leftChild is None and currentNode.rightChild is None:
                currentNode = None
            # case2
            if (currentNode.leftChild is None and currentNode.rightChild is not None) or (currentNode.leftChild is not None and currentNode.rightChild is None):
                if currentNode.leftChild is not None:
                    if parentNodeDirection == 'left':
                        parentNode.leftChild = currentNode.leftChild
                    else:
                        parentNode.rightChild = currentNode.leftChild
                else:
                    if parentNodeDirection == 'left':
                        parentNode.leftChild = currentNode.rightChild
                    else:
                        parentNode.rightChild = currentNode.rightChild
            # case3
            if currentNode.leftChild is not None and currentNode.rightChild is not None:
                # 1. 삭제 대상 노드의 오른쪽 서브트리 중 최소값(successor) 노드를 찾는다.
                successor = self.findSuccessor(currentNode.rightChild)
                # 2. successor 의 값을 삭제 대상 노드에 복사한다.
                currentNode.val = successor.val
                # 3. successor 노드를 삭제한다.
                return self.deleteNode(currentNode.rightChild, successor.val)
        else:
            return False

    def findSuccessor(self, node) -> Node:
        return self.findLowest(node)

    def findLowest(self, node) -> Node:
        if node.leftChild is not None:
            return self.findLowest(node.leftChild)
        if node.rightChild is not None:
            return self.findLowest(node.rightChild)
        return node
