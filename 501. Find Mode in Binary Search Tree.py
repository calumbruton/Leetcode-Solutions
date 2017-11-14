# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""Solution using O(n) additional memory and O(n) time complexity"""
class Solution(object):
    def findMode(self, root):
        if not root: return []
        
        self.dic = {}
        def inOrderTraversal(root):
            if not root: return None
            inOrderTraversal(root.left)
            if root.val in self.dic: 
                self.dic[root.val] += 1
            else: self.dic[root.val] = 1
            inOrderTraversal(root.right)
            return
        
        inOrderTraversal(root)
        count = max([x for z,x in self.dic.items()])
        mode = [val for val in self.dic if self.dic[val] == count]
        
        return mode