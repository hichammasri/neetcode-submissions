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
            return True, None, None

        # MinNode = root.val
        # MaxNode = root.val

        if not (root.left or root.right):
            return True, root.val, root.val


        validLeft, MinLeft, MaxLeft = self.isValidBSTMinMax(root.left)
        if not validLeft:
            return False, None, None
        if MaxLeft is not None and MaxLeft >= root.val:
            return False, None, None
        

        validRight, MinRight, MaxRight = self.isValidBSTMinMax(root.right)
        if not validRight:
            return False, None, None
        if MinRight is not None and MinRight <= root.val:
            return False, None, None
        print(root.val,MaxLeft, MinRight)
        if MinLeft is not None:
            MinNode = MinLeft
        else:
            MinNode = root.val
        if MaxRight is not None:
            MaxNode = MaxRight
        else:
            MaxNode = root.val
        return True, MinNode, MaxNode
        

        

        

        
        

        
        