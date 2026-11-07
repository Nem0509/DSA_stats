# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        cur=head
        nex = cur.next if cur is not None else None

        while cur is not None:

            cur.next=pre

            pre=cur
            cur=nex
            nex = cur.next if cur is not None else None
        return pre