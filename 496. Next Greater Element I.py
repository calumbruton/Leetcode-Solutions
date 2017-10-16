class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        O(n) time complexity solution
        """
        
        retMap = {}
        stack = []
        for num in nums:
            while stack!=[] and stack[-1] < num:
                retMap[stack.pop()] = num
            stack.append(num)
            
        # Get the nums val from the map and default to -1
        retArray = [retMap.get(num, -1) for num in findNums]  
        return retArray
                
        