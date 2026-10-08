# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = deque()
        curr = head
        while curr:
           nums.append(curr.val)
           curr = curr.next
        n = len(nums)
        if n == 0:
            return None
        k = k % n
        nums.rotate(k)
        dummy = ListNode(0)
        curr = dummy
        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next
    
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         n = 1
#         cur = head
#         while cur.next:
#             n += 1
#             cur = cur.next
#         cur.next = head

#         cur = head
#         for i in range(n - k%n -1):
#             cur = cur.next
#         head = cur.next
#         cur.next = None
#         return head