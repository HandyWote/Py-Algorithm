class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        st = set(nums)
        cur = dummy = ListNode(next=head)
        while cur.next:
            nxt = cur.next
            if nxt.val in st:
                cur.next = nxt.next  # 从链表中删除 nxt 节点
            else:
                cur = nxt  # 不删除 nxt，继续向后遍历链表
        return dummy.next
