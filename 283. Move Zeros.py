class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        zeroloc = 0 #location of leftmost zero
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[zeroloc] = nums[zeroloc], nums[i]
                zeroloc += 1 #zero has been moved up a location
            i += 1 # increment counter
        
        
        
        """
        Solution that does not maintain order of non zero elements!
        i = 0
        p = -1
        while i < len(nums)+:
            if nums[i] == 0:
                nums[i], nums[p] = nums[p], nums[i]
                p-=1
            
            i+=1
        """
