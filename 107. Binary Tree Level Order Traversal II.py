# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):

        self.levels = {}
        
        # A modified dfs method
        def dfs(root, level):
            if not root: return
            dfs(root.left, level+1)
            # Add the value to its to the levels array in the dict
            if level in self.levels:
                self.levels[level].append(root.val)
            else:
                self.levels[level] = [root.val]
            dfs(root.right, level+1)
              
        dfs(root, 0)
        # return the reversed list of all levels
        order = reversed([x for x in self.levels])
        
        # Fill the result array with an array for each level
        result = []
        for i in order:
            result.append([val for val in self.levels[i]])
        return result
        
        