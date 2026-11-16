# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # O(1): always sorting 2 values
        s, l = sorted([p.val, q.val])

        node = root

        while root:
            if s <= root.val and l>= root.val:
                return root
            elif s>= root.val:
                root = root.right
            else:
                root = root.left
        