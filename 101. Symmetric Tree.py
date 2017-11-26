# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        
        if not root: return True
    
        def symmetric(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            else:
                if left.val == right.val:
                    return symmetric(left.left, right.right) and symmetric(left.right, right.left)
                else:
                    return False
    
        return symmetric(root.left, root.right)