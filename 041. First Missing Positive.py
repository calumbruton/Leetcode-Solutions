class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        O(n) running time and constant space
        """
        minV = 10000000
        maxV = 0
        
        pos = 0
        for x in nums:
            if x > 0:
                if x < minV:
                    minV = x
                if x > maxV:
                    maxV = x
            
        # If 1 was not present 
        if minV > 1:
            return 1    
        
        # If it was check the range from min to max for first missing value
        for y in range(minV,maxV):
            print(y)
            if y not in nums:
                return y
        
        # If no missing value then return the max pos + 1
        return maxV+1