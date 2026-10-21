# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s=[]
        if not root:
            return 0
        s.append([root,1])
        ans=0

        while s:
            n=s.pop()
            ans=max(ans,n[1])
            if n[0].left:
                s.append([n[0].left,n[1]+1])
            if n[0].right:
                s.append([n[0].right,n[1]+1])
        
        return ans