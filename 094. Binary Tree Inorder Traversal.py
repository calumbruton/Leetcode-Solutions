# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        nodes = []
        seenLeft = set()
        seenRight = set()
        nodes.append(root)
        
        while len(nodes) != 0 and root:
            root = nodes.pop()
            if root.left and root not in seenLeft:
                print("Going left: ", root.val)
                nodes.extend([root, root.left])
                seenLeft.add(root)
                root = root.left
            elif root.right and root not in seenRight:
                print("Going right: ", root.val)
                ans.append(root.val)
                nodes.extend([root, root.right])
                seenRight.add(root)
                root = root.right
            elif root not in seenRight:
                ans.append(root.val)
            
        return ans