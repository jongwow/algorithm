from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printNode(head: Optional[ListNode]):
    while head != None:
        print(head.val)
        head = head.next
    print('---')


def printNode2(head: Optional[ListNode]):
    while head != None:
        print(head.val, end=', ')
        head = head.next
    print()


class Solution:
    # 1938 ~ 1942
    def sortListV1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        current = head
        while current != None:
            res.append(current.val)
            current = current.next
        res.sort()
        if len(res) == 0:
            return None

        prev = ListNode(res[0])
        new_head = prev
        idx = 1
        while idx < len(res):
            cur = ListNode(res[idx])
            prev.next = cur
            prev = cur
            idx += 1
        return new_head
    # 2031 ~ 2039, timeLimit

    def sortListV2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        new_head = ListNode(head.val)
        # head = head.next
        while head != None:
            inner_prev = new_head
            current_value = head.val
            while inner_prev.next != None and inner_prev.next.val < current_value:
                inner_prev = inner_prev.next
            new_node = ListNode(current_value)
            next_node = inner_prev.next
            inner_prev.next = new_node
            new_node.next = next_node
            head = head.next
        return new_head.next

    # 2042 ~ ...(한 한시간?)
    def sortListV3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        cnt = 0
        p = head
        while p != None:
            cnt += 1
            p = p.next
        result = self.halfSort(head, cnt)
        return result

    def halfSort(self, node: Optional[ListNode], nodeCnt: int) -> Optional[ListNode]:
        if nodeCnt == 0:
            return None
        if nodeCnt == 1:
            return ListNode(node.val)
        if nodeCnt == 2:
            head = node
            tail = node.next
            if head.val < tail.val:
                return ListNode(head.val, ListNode(tail.val))
            else:
                return ListNode(tail.val, ListNode(head.val))
        left_cnt = nodeCnt // 2
        right_cnt = nodeCnt - left_cnt
        pivot_node = node
        right_node = node
        count = 1
        while count < left_cnt:
            pivot_node = pivot_node.next
            count += 1
        right_node = pivot_node.next
        pivot_node.next = None
        left = self.halfSort(node, left_cnt)
        right = self.halfSort(right_node, right_cnt)

        result_node = self.mergeList(left, right)
        return result_node

    def mergeList(self, leftNode: Optional[ListNode], rightNode: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if leftNode is None:
            return rightNode
        if rightNode is None:
            return leftNode
        # recursive case
        result_node_head = None
        result_node = None
        if leftNode.val < rightNode.val:
            result_node = ListNode(leftNode.val)
            leftNode = leftNode.next
            result_node_head = result_node
        else:
            result_node = ListNode(rightNode.val)
            rightNode = rightNode.next
            result_node_head = result_node
        while (leftNode is not None) and (rightNode is not None):
            if leftNode.val < rightNode.val:
                new_node = ListNode(leftNode.val)
                leftNode = leftNode.next
            else:
                new_node = ListNode(rightNode.val)
                rightNode = rightNode.next
            result_node.next = new_node
            result_node = result_node.next
        while (leftNode is not None):
            new_node = ListNode(leftNode.val)
            leftNode = leftNode.next
            result_node.next = new_node
            result_node = result_node.next
        while (rightNode is not None):
            new_node = ListNode(rightNode.val)
            rightNode = rightNode.next
            result_node.next = new_node
            result_node = result_node.next
        return result_node_head


sol = Solution()
# a = ListNode(3)
# b = ListNode(5)
# c = ListNode(8)
# d = ListNode(2)
# e = ListNode(4)
a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
d = ListNode(3)
e = None
# e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
# res = sol.halfSort(a, 2)
res = sol.sortListV4(a)
print()
printNode(res)
