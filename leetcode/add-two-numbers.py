from typing import List, Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 0039~0058

    def addTwoNumbersV1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def listToNum(l):
            res = 0
            while len(l) != 0:
                n = l.pop(0)
                res += n
                res *= 10
            return res // 10

        def linkedListToList(ll):
            res = []
            while ll.next != None:
                res.append(ll.val)
                ll = ll.next
            res.append(ll.val)
            return res

        def listToLL(l):
            if len(l) == 1:
                return ListNode(l[0])
            idx = 1
            root = ListNode(l[0])
            cur = root
            while idx < len(l):
                cur.next = ListNode(l[idx])
                cur = cur.next
                idx += 1
            return root
        l1List = []
        while l1.next != None:
            l1List.append(l1.val)
            l1 = l1.next
        l1List.append(l1.val)
        l2List = []
        while l2.next != None:
            l2List.append(l2.val)
            l2 = l2.next
        l2List.append(l2.val)
        l1List = listToNum(list(reversed(l1List)))
        l2List = listToNum(list(reversed(l2List)))
        l3 = l1List+l2List
        res = list(reversed(list(map(int, str(l3)))))
        res = listToLL(res)
        return res
# 0100~0110

    def addTwoNumbersV2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        current = ListNode(0)
        root = current
        while l1 != None or l2 != None:
            l3Val = 0
            if carry:
                l3Val += 1
                carry = 0
            if l1 != None and l2 != None:
                l3Val += l1.val+l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1 != None and l2 == None:
                l3Val += l1.val
                l1 = l1.next
            elif l1 == None and l2 != None:
                l3Val += l2.val
                l2 = l2.next
            if l3Val >= 10:
                carry = 1
                l3Val -= 10
            current.next = ListNode(l3Val)
            current = current.next
        if carry:
            current.next = ListNode(carry)
        return root.next


def linkedListToList(ll):
    res = []
    if ll == None:
        return []
    while ll != None:
        res.append(ll.val)
        ll = ll.next
    return res


sol = Solution().addTwoNumbersV2(ListNode(2, ListNode(4, ListNode(3))),
                                 ListNode(5, ListNode(6, ListNode(4))))
print(linkedListToList(sol))
