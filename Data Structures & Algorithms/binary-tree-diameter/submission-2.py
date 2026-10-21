# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        llst,rlst=[],[]
        llst.append(root)
        while True:
            if llst[-1].left is None and llst[-1].right is None:
                break
            if llst[-1].left is not None:
                llst.append(llst[-1].left)
            else:
                llst.append(llst[-1].right)
        rlst.append(root)
        while True:
            if rlst[-1].left is None and rlst[-1].right is None:
                break
            if rlst[-1].right is not None:
                rlst.append(rlst[-1].right)
            else:
                rlst.append(rlst[-1].left)

        same=0
        j=min(len(llst),len(rlst))
        for i in range(1,j):
            if llst[i] is rlst[i]:
                same=i
        if len(llst)==len(rlst) and len(rlst)==same+1:
            return same
        return len(llst)-same+len(rlst)-same-2

            