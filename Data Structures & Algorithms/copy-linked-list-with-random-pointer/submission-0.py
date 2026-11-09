"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic={}

        nhead=Node(0,None,None)
        ans=nhead

        while head:
            nhead.next=Node(0,None,None)
            nhead=nhead.next
            nhead.val=head.val
            dic[head]=nhead
            head=head.next

        for k,v in dic.items():
            if k.random:
                v.random=dic[k.random]
        
        return ans.next
