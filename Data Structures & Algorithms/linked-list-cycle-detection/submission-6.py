# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p=head.next if head is not None else None
        p=p.next if p is not None else None

        while head and p and head is not p:
            head=head.next if head is not None else None
            p=p.next if p is not None else None
            p=p.next if p is not None else None
        return head is not None and p is not None

        
        
