# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cnt=1000
        while head:
            if cnt<0:
                return True
            head=head.next
            cnt-=1
        return False