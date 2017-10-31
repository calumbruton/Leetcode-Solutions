class Solution(object):
    def findDisappearedNumbers(self, nums):
        """The O(n) additional space easy solution"""
        x = set()
        n = len(nums)
        for num in nums:
            if num not in x:
                x.add(num)
        return [num for num in range(1,n+1) if num not in x]        
        
        