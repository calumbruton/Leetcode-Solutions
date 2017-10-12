class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = set()
        for x in nums:
            if x in n:
                n.remove(x)
            else:
                n.add(x)
                
        return n.pop()