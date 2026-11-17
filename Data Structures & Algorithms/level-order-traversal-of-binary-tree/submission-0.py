# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        traverseQueue = deque([(root,0)])
        result = defaultdict(list)

        while traverseQueue:
            node, level = traverseQueue.popleft()
            if node:
                result[level].append(node.val)
                if node.left:
                    traverseQueue.append((node.left, level+1))
                if node.right:
                    traverseQueue.append((node.right, level+1))
        return list(result.values())



        