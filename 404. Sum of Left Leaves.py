# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if root.left != None:
            # If the left node is a leaf then return its value and recurse down the right side
            if (root.left.left == None and root.left.right == None):
                return root.left.val + self.sumOfLeftLeaves(root.right)
            # Else continue recursing down the left and right side
            else:
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
        # Else there is no left node continue recursing down the right side
        else:
            return self.sumOfLeftLeaves(root.right)
        