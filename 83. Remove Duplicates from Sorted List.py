# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        lastval = None
        lastNode = None
        
        node = head
        while node:
            if node.val == lastval:
                lastnode.next = node.next
            
            else:
                lastval = node.val
                lastnode = node
            
            node = node.next
            
        return head