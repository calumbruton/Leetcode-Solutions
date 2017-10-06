class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        """O(n) one line solution using list comprehension"""
        return len([x for x in nums if x < target])
        