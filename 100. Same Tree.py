# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #Base case no value
        if p==None or q==None:
            if p!=None or q!=None:
                return False
        
        # if the values in the nodes are not equal
        elif p.val != q.val:
            return False
        
        # recurse down each side of the tree
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return True