from typing import List, Optional
from collections import deque

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroupV1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Memory 신경 안쓰고.
        if head == None:
            return None
        current_node = head
        current_list = []
        inner_list = deque()
        cnt = 0
        while current_node != None:
            cnt += 1
            current_list.append(current_node.val)
            current_node = current_node.next
            if cnt % k == 0:
                while len(current_list) > 0 and cnt > 0:
                    cnt -= 1
                    val = current_list.pop()
                    inner_list.append(val)
                if cnt == 0:
                    while len(inner_list) > 0:
                        val = inner_list.popleft()
                        current_list.append(val)
                else:
                    while len(inner_list) > 0:
                        val = inner_list.pop()
                        current_list.append(val)
        # construct ListNode
        idx = 0
        newHead = ListNode(current_list[idx])
        cursor = newHead
        idx += 1
        print(current_list)
        while idx < len(current_list):
            cursor.next = ListNode(current_list[idx])
            cursor = cursor.next
            idx += 1
        return newHead

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        prev_group_end = None
        group_start = head
        cnt = 0
        while current != None:
            print('current: ', current.val)
            cnt += 1
            if cnt == k:
                prev_group_end.next = current  # 4가 8을 가리키도록 하고
                prev_group_end = group_start  # 8 을 저장하고
                next_group_start = current.next
                prev_cursor = current.next  # 9 를 prev_cursor로 정의
                cursor = group_start  # cursor 는 group의 시작
                while cursor != next_group_start:
                    next_cursor = cursor.next
                    cursor.next = prev_cursor
                    prev_cursor = cursor
                    cursor = next_cursor
                print("PREV")
                verification(prev_cursor)
                cnt = 0
                current = next_group_start
            else:
                if cnt == k-1:
                    prev_group_end = current
                current = current.next
        return head


def verification(head: Optional[ListNode]):
    while head != None:
        print(head.val, end=',')
        head = head.next
    print()


head = ListNode(1)
CNT = 10
cur = head
for i in range(2, CNT + 1):
    elem = ListNode(i)
    cur.next = elem
    cur = elem

verification(head)
print('k:', 4)
print('--------')
ans = Solution().reverseKGroup(head, 4)
verification(ans)

# prev_cursor = None
# cursor = head
# while cursor != None:
#     next_cursor = cursor.next
#     cursor.next = prev_cursor
#     prev_cursor = cursor
#     cursor = next_cursor
# return prev_cursor
