class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numSet = set()
        for x in nums1:
            if x not in numSet:
                numSet.add(x)
        
        retArr = []
        for x in nums2:
            if x in numSet:
                retArr.append(x)
                numSet.remove(x)
                
        return retArr