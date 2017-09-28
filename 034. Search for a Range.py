class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Using binary search to find the element then moving up and down the original list of nums from 
        that index until the values are no longer the target value, this gives the range of indices
        This is an O(logn) solution
        """
        n = len(nums)
        vals = nums
        i = 0
        
        found = False
        while not found:
            y = len(vals)
            if y<1: return [-1,-1]
            
            x = y/2
            if vals[x] == target:
                i += x
                found = True
            elif target < vals[x]:
                vals = vals[:x]
            else:
                vals = vals[x+1:]
                i += x+1
        
        low = i
        high = i
        while low>0 and nums[low-1] == target:
            low -= 1
        while high < n-1 and nums[high+1] == target:
            high += 1
            
        return [low,high]
                