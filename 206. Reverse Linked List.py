# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        O(n) performance
        """
    
        lastNode = None
        while head:
            newNode = head
            head = head.next
            newNode.next = lastNode
            lastNode = newNode
        
        return lastNode
    
        