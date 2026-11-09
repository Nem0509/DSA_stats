# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head if head is None else head.next
        
        slow=head
        cnt=0
        while slow:
            cnt+=1
            slow=slow.next

        i=cnt-n-1
        p=head

        if i <0:
            temp=head
            head=head.next
            temp.next=None
            return head

        for f in range(i):
            p=p.next

        temp=p.next
        p.next=temp.next
        temp.next=None

        return head

            



        