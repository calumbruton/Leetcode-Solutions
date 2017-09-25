# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        
        #If one or no nodes 
        if head == None or head.next == None:
            return head
        
        # Pointers
        head = head.next
        trailer = None
        
        #While there is a next node and next next node
        while temp and temp.next != None:
            if trailer:
                trailer.next = temp.next
            temp1 = temp.next.next
            temp.next.next = temp
            temp.next = temp1
                
            trailer = temp
            temp = temp.next
        
        return head