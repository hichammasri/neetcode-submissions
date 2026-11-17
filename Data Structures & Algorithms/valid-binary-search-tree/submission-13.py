# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.isValidBSTMinMax(root)[0]
    
    def isValidBSTMinMax(self, root: Optional[TreeNode]) ->tuple(bool, int, int):
        if not root:
            return True, float("+inf"), float("-inf")

        if not (root.left or root.right):
            return True, root.val, root.val


        validLeft, MinLeft, MaxLeft = self.isValidBSTMinMax(root.left)
        if not validLeft:
            return False, None, None
        if MaxLeft >= root.val:
            return False, None, None
        

        validRight, MinRight, MaxRight = self.isValidBSTMinMax(root.right)
        if not validRight:
            return False, None, None
        if MinRight <= root.val:
            return False, None, None

        return True, min(MinLeft, root.val), max(MaxRight, root.val)
        

        

        

        
        

        
        