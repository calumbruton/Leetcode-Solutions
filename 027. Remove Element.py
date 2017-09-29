class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        #Slice operator is necessary to alter list in place in python
        nums[:] = [x for x in nums if x != val]
        return len(nums)
        
        
        