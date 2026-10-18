# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        s=[]
        s.append(root)
        while s:
            n=s.pop()
            n.left,n.right=n.right,n.left
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)
        return root