class Solution(object):
    def findPeakElement(self, nums):
        """
        Brute force solution O(n) complexity. Potential for improvement by checking first and last element first
        then starting at a center element and moving in left or right depending on which direction an element is larger
        """
        
        #If the list has one element
        if len(nums) == 1:
            return 0
        
        for x in range(len(nums)):
            
            # edge case first element
            if x == 0:
                if nums[x] > nums[x+1]:
                    return 0
            
            # edge case last element
            elif x == (len(nums)-1):
                if nums[x] > nums[x-1]:
                    return x
            
            else:
                if nums[x] > nums[x-1] and nums[x] > nums[x+1]:
                    return x
    
        return 0

