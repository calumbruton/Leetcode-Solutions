class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        dup = None
        for x in nums:
            if x in s:
                dup = x
            s.add(x)
            
        for i in range(1,len(nums)+1):
            if i not in s:
                return [dup,i]