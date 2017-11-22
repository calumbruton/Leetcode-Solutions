# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        
        if not root: return
        
        l_level = {}
        def dfs(root,level):
            if not root: return
            
            if level not in l_level:
                l_level[level] = root.val
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        dfs(root,0)
        return l_level[max([l for l in l_level])]
        
        