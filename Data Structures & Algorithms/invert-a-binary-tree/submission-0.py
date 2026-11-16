# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not (root and (root.left or root.right)):
            return root
        
        traverseQueue = deque()
        traverseQueue.append(root)

        while len(traverseQueue)>0:
            node = traverseQueue.popleft()
            if node.left:
                traverseQueue.append(node.left)
            if node.right:
                traverseQueue.append(node.right)
            
            tmp = node.left
            node.left = node.right
            node.right = tmp
        
        return root



            
        