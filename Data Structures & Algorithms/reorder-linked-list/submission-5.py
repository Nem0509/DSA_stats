# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.val)

        prev=None
        cur=slow

        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp

        temp=head
        while temp:
            a=temp.next
            temp.next=prev
            b=prev.next
            prev.next=a
            temp=a
            prev=b


