# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs (node, l = []):
            """depth first search function to return a list of ordered elements from a BST"""
            if node.left: dfs(node.left, l)
            l.append(node.val)
            if node.right: dfs(node.right, l)
            return l
        
        # Get ordered elements array and use list comprehension to find minimum absolute difference
        l = dfs(root)
        n = min(list(reduce(lambda a, b: abs(a-b) ,group) for group in zip(l, l[1:])))
            
        return n
        