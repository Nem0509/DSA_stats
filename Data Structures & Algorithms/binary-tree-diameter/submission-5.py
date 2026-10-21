# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        c=0
        lp=root
        rp=root
        while True:
            if lp.left is None and lp.right is None and rp.right is None and rp.left is None:
                break
            if lp.left is not None:
                lp=lp.left
                c+=1
            elif lp.right is not None:
                lp=lp.right
                c+=1
            if rp.right is not None:
                rp=rp.right
                c+=1
            elif rp.left is not None:
                rp=rp.left
                c+=1
            if lp is rp:
                c=0
        def rec(root):
            if not root:
                return 0
            return 1+max(rec(root.left),rec(root.right))
        d=rec(root)

        return max(c,d-1)
        