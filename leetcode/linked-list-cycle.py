from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head
        while tortoise != None and hare != None:
            tortoise = tortoise.next
            hare = hare.next
            if hare != None:
                hare = hare.next
            else:
                return False
            if tortoise == hare:
                return True
        return False

    def hasCycleV1(self, head: Optional[ListNode]) -> bool:
        cur = head
        visited = set([])
        while cur != None and cur.next != None:
            # print(cur.val)
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        return False


e1 = ListNode(3)
e2 = ListNode(2)
e3 = ListNode(0)
e4 = ListNode(-4)
e1.next = e2
e2.next = e3
e3.next = e4
e4.next = e2


sol = Solution().hasCycle(e1)
print(sol)
