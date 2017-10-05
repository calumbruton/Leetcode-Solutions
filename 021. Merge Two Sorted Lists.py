# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Base cases
        if not l1 or not l2:
            return l1 or l2
        
        # Initialize head based on smallest variable
        if l1.val < l2.val: 
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        # The static pointer to the first node in the 
        returnHead = head
        
        # While the linked lists have items check which value is smaller and add it to the linked list
        while l1 and l2:
            if l1.val<l2.val: 
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        
        # Make the rest of the linked list the rest of the items in the linked list remaining
        if l1:
            head.next = l1
        else:
            head.next = l2
        
        return returnHead