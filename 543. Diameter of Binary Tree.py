# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.best = 0
        def depth(root):
            if not root: return 0
            left = depth(root.left)
            right = depth(root.right)
            # Is the depths of the left and right path from this node
            # greater than the best seen so far
            self.best = max(self.best, left+right)
            return 1+max(left,right)
        depth(root)
        return self.best
        