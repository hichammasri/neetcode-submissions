# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        sortedTree = []
        self.sortTree(root, sortedTree, k)
        return sortedTree[k-1]
        

    def sortTree(self, root: Optional[TreeNode], sortedOutput: list, k:int) -> None:

        if not root:
            return
        if len(sortedOutput) == k:
            return
        if not (root.left or root.right):
            sortedOutput.append(root.val)
            return
        
        self.sortTree(root.left, sortedOutput, k)
        sortedOutput.append(root.val)
        self.sortTree(root.right, sortedOutput, k)
        
        




        